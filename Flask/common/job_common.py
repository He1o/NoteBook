"""Some common classes for job."""
# pylint: disable=R0902,W0703
from typing import (Callable, Dict, List, Tuple)

from Flask.common.common import (ObjectWithTrace, JobConf,
                                     StrategyStatusCode)
from Flask.common.context import context
from Flask.common.strategy_manager import StrategyBase, StrategyManager
from Flask.common.error import Error
from Flask.common.trace import Trace
from Flask.common import utils


class StrategyStatus(object):
  """Strategy status ."""
  def __init__(self, stg_name: str, start_time_stamp: int, total_step_cnt: int,
               last_step: int, last_timestamp: int):
    self.stg_name = stg_name
    self.start_time_stamp = start_time_stamp
    self.total_step_cnt = total_step_cnt
    self.last_step = last_step
    self.last_timestamp = last_timestamp
    self.last_func_name = ""
    self.last_succ: bool = False
    self.last_runned: bool = False
    self.last_status_code: StrategyStatusCode = StrategyStatusCode.Unknown
    self.last_step_time_cost = 0
    self.total_time_cost = 0
    self.total_step_succed_cnt = 0
    self.total_run_cnt = 0
    self.done = False
    self.progress = 0.0
    self.succ = False
    self.last_step_status_code = 0
    self.last_step_runned = False
    self.last_step_succ = False
    self.last_time_cost = 0

  def update(self, step: int, func_name: str, err: Error, runed: bool,
             status_code: StrategyStatusCode) -> int:
    """Update parameters."""
    current_time = utils.get_timestamp(use_ms=True)
    self.last_time_cost = current_time - self.last_timestamp
    self.total_time_cost = current_time - self.start_time_stamp
    self.last_step = step
    self.last_func_name = func_name
    self.last_step_succ = True if err is None else False
    self.last_step_runned = runed
    self.last_step_status_code = status_code
    self.last_timestamp = current_time
    self.last_step_time_cost = utils.get_timestamp(
        use_ms=True) - self.last_timestamp
    self.progress = (self.last_step + 1) * 1.0 / self.total_step_cnt
    if self.last_step == self.total_step_cnt - 1:
      self.done = True
    if self.done and self.last_step_status_code == StrategyStatusCode.Success:
      self.succ = True
    if self.last_step_succ:
      self.total_step_succed_cnt += 1
    if self.last_step_runned:
      self.total_run_cnt += 1

  def status_msg(self) -> bool:
    """Make status message."""
    msg = []
    msg.append(f"stg_name={self.stg_name}")
    msg.append(f"total_step_cnt={self.total_step_cnt}")
    msg.append(f"func_name={self.last_func_name}")
    msg.append(f"last_step={self.last_step}")
    msg.append(f"step_time_cost={self.last_step_time_cost}")
    msg.append(f"step_succ={self.last_step_succ}")
    msg.append(f"step_runed={self.last_step_runned}")
    msg.append(f"step_status_code={self.last_step_status_code}")
    msg.append(f"total_runed_cnt={self.total_run_cnt}")
    msg.append(f"total_succed_cnt={self.total_step_succed_cnt}")
    msg.append(f"done={self.done}")
    msg.append(f"progess={self.progress}")
    msg.append(f"succ={self.succ}")
    return ", ".join(msg)


class JobItem(ObjectWithTrace):
  """Job item represents exactly what strategies will be implemented."""
  def __init__(self,
               job_conf: JobConf = JobConf(),
               trace: Trace = Trace(),
               region: str = "cn"):
    super().__init__(trace=trace if trace is not None else Trace())
    self._job_conf: JobConf = job_conf
    self._region = region
    self.stg_names: List[str] = []
    self.stgs: List[StrategyBase] = []
    self._execute_lists: List[List[Callable]] = []
    self._status: Dict[str, StrategyStatus] = {}
    self._log_id = self.get_log_id()
    self.start_timestamp = utils.get_timestamp(use_ms=True)

  def init_strategies(self) -> bool:
    """Init strategies and status."""
    if not self.__init_strategies():
      self.error("JobItem_init_strategies_error.")
      return False
    if not self.__init_status():
      self.error("JobItem_init_status_error.")
      return False
    return True

  def get_log_id(self):
    """Gets log id."""
    return (f"jobItem-{self._trace.trace()}-"
            f"{self._job_conf.id}-{self._region}-{context.env()}")

  def __init_strategies(self) -> bool:
    """Inner function for init strategies."""
    for strategy_name in self._job_conf.strategy_names_ori:
      stg: StrategyBase = StrategyManager.get_instance().get_strategy_by_name(
          strategy_name)
      if stg is None:
        self.error(f"Job_item_init_error, stg_none, name={strategy_name}")
        return False
      if context.product_env():
        try:
          succ = stg.reset(job_conf=self._job_conf,
                           trace=self._trace)
        except Exception as e:
          succ = False
          self.error(f"Job_item_init_error, crash, job={self._job_conf.id}, "
                     f"stg_name={strategy_name}, succ={succ}, err={e.args}")
      else:
        succ = stg.reset(job_conf=self._job_conf,
                         trace=self._trace)
      if not succ:
        self.error(f"Job_item_init_error, job={self._job_conf.id}, "
                   f"stg_name={strategy_name}, succ={succ}")
        continue
      self.stg_names.append(strategy_name)
      self.stgs.append(stg)
      self._execute_lists.append(stg.execute_list())
      if len(self.stg_names) != len(self._execute_lists):
        self.error("Job_item_init_error, execute_list size not match.")
        return False
    return True

  def valid(self) -> bool:  # pylint: disable=R0201
    """Reserve."""
    return True

  def __init_status(self) -> bool:
    """Inner function for init status."""
    current_timestamp = utils.get_timestamp(use_ms=True)
    for stg_idx in range(len(self.stg_names)):
      stg_name = self.stg_names[stg_idx]
      self._status[stg_name] = StrategyStatus(
          stg_name=stg_name,
          start_time_stamp=current_timestamp,
          total_step_cnt=len(self._execute_lists[stg_idx]),
          last_step=-1,
          last_timestamp=current_timestamp)
    return True

  def update_status(self, stg_name: str, finished_func: Callable,
                    finished_step: int, err: Error, runed: bool,
                    status_code: StrategyStatusCode) -> bool:
    """Update status."""
    if stg_name not in self._status:
      self.error(f"Job_status_update_failed, error=stg_name_not_finded, "
                 f"stg_name={stg_name}")
      return False
    stg_status = self._status[stg_name]
    stg_status.update(step=finished_step,
                      func_name=utils.get_func_name(finished_func),
                      err=err,
                      runed=runed,
                      status_code=status_code)
    self.monitor(f"Job_status_update_succ, {stg_status.status_msg()}")
    if stg_status.done:
      self.monitor(f"Job_status_update_all_finished, {stg_status.status_msg()}")
    return True

  def done(self) -> bool:
    """Whether done."""
    return len([
        stg_name for stg_name in self._status if not self._status[stg_name].done
    ]) == 0

  def progress(self) -> Tuple[float, float]:
    """Output the progress of the job."""
    finished_ratio = len([
        self._status[stg_name]
        for stg_name in self._status
        if self._status[stg_name].done
    ]) * 1.0 / (len(self._status) + 0.01)
    status = [self._status[stg_name].progress for stg_name in self._status]
    min_progress = 0.0 if len(status) < 1 else min(status)
    return finished_ratio, min_progress

  def succ(self) -> bool:
    """Check whether is success."""
    succ = True
    for stg_status in self._status.values():
      self.monitor(f"Job_stg_final_status, {stg_status.status_msg()}")
      # TODO(zhanshushi): Need to judge with priority?
      if not stg_status.succ:
        succ = False
    self.monitor(f"Job_final_status, succ={succ}")
    return succ

  @property
  def id(self):
    """Builds an string with the relevant information as id."""
    info = (f"trace={self._trace.trace()}_job={self._job_conf.id}_"
            f"region={self._region}_run_mode={context.env()}")
    return info

  @property
  def execute_lists(self):
    """Execute lists."""
    return self._execute_lists
