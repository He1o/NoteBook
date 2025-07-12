"""Generator is the entry of the whole project."""
from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from functools import partial
from typing import List, Dict

from Flask.common.common import JobConf, RunMode
from Flask.common.context import context, _init_context
from Flask.common.host_env import get_host_env
from Flask.common.trace import (Trace)
from Flask.common.job_common import JobItem
from Flask.common.log_tools import logger
from Flask.common.strategy_processor import JobProcessor
from Flask.common import init, log_tools, utils


class Generator(object):
  """The entrance to init all environment and start all the tasks."""
  pool_executor = ThreadPoolExecutor(2)
  test_flag = False
  runing_futures: Dict[str, JobItem] = {}
  region: str = "Regions.CN"

  @classmethod
  def init_generator(cls, region: str = "Regions.CN"):
    """Init strategy manager and database's client."""
    cls.region = region
    init.init_strategy_manager()
    init.init_client(region=region)
    logger.info(
        f"init generator done, region={cls.region}, env={context.env()}.")

  @classmethod
  def done_callback(cls, future: Future, job_item: JobItem):
    """The callback after task done."""
    current_time = utils.get_timestamp(use_ms=True)
    time_cost = current_time - job_item.start_timestamp
    succ = future.result()
    if not succ:
      logger.error("Generator_job_process_failed, "
                   f"job_succ={succ}, job={job_item.id}, time_cost={time_cost}")
    cls.runing_futures.pop(job_item.id)
    logger.info(f"Generator_job_process_succed, job_succ={succ}, "
                f"job_done={job_item.done()}, "
                f"job_progress={job_item.progress()}, "
                f"job={job_item.id}, still_runing={len(cls.runing_futures)}")

  @classmethod
  def process_job(cls, job_item: JobItem) -> bool:
    """Trigger the job start."""
    processor = JobProcessor(job_item=job_item)
    if not processor.do():
      return False
    return True

  @classmethod
  def generate(cls, job_confs: List[JobConf], trace: Trace):
    """Trigger all the jobs start."""
    futures: Dict[Future, str] = {}
    for job_conf in job_confs:
      job_item = JobItem(job_conf=job_conf, trace=trace)
      if not job_item.init_strategies():
        logger.error("PriorMapGenerator,generate_new, "
                     f"jobitem init error, job={job_conf.id} ")
        continue
      future = cls.pool_executor.submit(Generator.process_job, job_item)
      futures[future] = job_item
      cls.runing_futures[job_item.id] = job_item

    for future in as_completed(futures):
      future.add_done_callback(
          partial(Generator.done_callback, job_item=futures[future]))

  @staticmethod
  def init_logging(level: int = None, format_in: str = None):
    """Init logging."""
    log_tools.init_logging(level=level, logging_format=format_in)

  @staticmethod
  def init_context(project_dir: str = "",
                   build_dir: str = "",
                   tmp_dir: str = "",
                   run_mode: RunMode = RunMode.PRODUCTION):
    """Iinit logging."""
    _init_context(
        project_dir=project_dir,
        build_dir=build_dir,
        tmp_dir=tmp_dir,
        run_mode=run_mode)


if __name__ == "__main__":
  job_confs_out = [
      JobConf(
          city_id=9,
          map_region="guangzhou",
          strategy_names=["test_speed", "test_speed_eval", "test_upload_data"],
          # tid="20220607060",
          # mini_run=True,
          run_imediately=True),
      JobConf(
          city_id=1,
          map_region="beijing_yizhuang",
          strategy_names=["test_speed", "test_speed_eval", "test_upload_data"],
          # tid="20220607060",
          # mini_run=True,
          run_imediately=True
      ),
  ]
  Generator.init_context(run_mode=get_host_env())
  Generator.init_logging()
  Generator.init_generator(region=Regions.from_timezone())
  Generator.generate(job_confs=job_confs_out, trace=Trace())
