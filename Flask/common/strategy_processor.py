"""Job processor class."""
from functools import partial
from concurrent.futures import ThreadPoolExecutor, as_completed
from Flask.common import utils
from Flask.common.common import ObjectWithTrace
from Flask.common.context import context
from Flask.common.data_manager import DataManager
from Flask.common.job_common import JobItem
from Flask.common.trace import Trace


class JobProcessor(ObjectWithTrace):
  """Responsible for job execution."""
  def __init__(self, job_item: JobItem = JobItem(), processor_id=""):
    super().__init__(
        trace=job_item.trace if job_item.trace is not None else Trace(
            f"JobProcessor_{processor_id}"))
    self._data_manager = DataManager(thread_pool_size=10, trace=self._trace)
    self._job_item = job_item
    self._processor_id = processor_id
    self._log_id = self.get_job_process_log_id()
    self._process_pool = ThreadPoolExecutor(max_workers=4)

  def reset(self, job_item: JobItem) -> bool:
    """Reset parameters."""
    self._data_manager.reset()
    self._job_item = job_item
    self._log_id = self.get_job_process_log_id()
    return True

  def do(self) -> bool:
    """Excutes all strategies."""
    all_strategy_finished = False
    step = 0
    strategy_finished_flags = [False] * len(self._job_item.execute_lists)
    while not all_strategy_finished:
      futures = {}
      for stg_idx in range(len(self._job_item.execute_lists)):
        if step == len(self._job_item.execute_lists[stg_idx]):
          strategy_finished_flags[stg_idx] = True
          continue
        if strategy_finished_flags[stg_idx]:
          continue
        execute_func = self._job_item.execute_lists[stg_idx][step]
        future = self._process_pool.submit(
                                           partial(utils.func_executor,
                                                   execute_func,
                                                   context.product_env()),
                                           self._data_manager)
        futures[future] = (stg_idx, execute_func)
        self.debug(f"Processor_func_exec, step={step},"
                   f"future={future},futures=[{futures}]")
      if not futures:
        all_strategy_finished = True
        break

      # TODO(zhanshushi): who ends? what if some one not end?
      # if someone error, stop the corresponding strategy.
      for future in as_completed(futures):
        stg_idx, execute_func = futures[future]
        stg_name = self._job_item.stg_names[stg_idx]
        error, runed, status_code = future.result()
        self._job_item.update_status(
            stg_name=stg_name,
            finished_func=execute_func,
            finished_step=step,
            err=error,
            runed=runed,
            status_code=status_code)
        if error is not None:
          strategy_finished_flags[stg_idx] = True
          self.error(f"Processor_func_exec_failed, stg_name={stg_name}" +
                     f", step={step}" + f", error={error.str}, " +
                     f"runed={runed}, status_code={status_code}")
          continue
        self.info("Processor_func_exec_successed, "
                  f"job={self._job_item.id}, stg_name={stg_name}"
                  f", step={step}"
                  f", execute_func={utils.get_func_name(execute_func)}"
                  f", runed={runed}, status_code={status_code}")
      self._data_manager.do()
      step += 1
    return self._job_item.succ()

  def get_job_process_log_id(self):  # pylint: disable=W0221
    """Gets job process log id."""
    log_id = (f"JobProcessor_trace={self._trace.trace()}_"
              f"processor={self._processor_id}_job={self._job_item.id}")
    return log_id

  @property
  def processor_id(self):
    """_processor_id."""
    return self._processor_id
