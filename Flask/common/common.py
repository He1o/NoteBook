"""Define some common and basic class."""
from enum import Enum
from typing import List
from Flask.common.context import RunMode
from Flask.common.log_tools import logger
from Flask.common.trace import Trace


class ObjectWithlog(object):
  """Log with log_id."""
  _log_id = "ObjectWithlog"

  def __init__(self, log_id: str = "") -> None:
    if log_id is not None and log_id.strip():
      self._log_id = log_id

  def get_job_process_log_id(self, suffix: str):
    """Gets log id."""
    self._log_id += f"_{suffix}"
    return self._log_id

  def debug(self, msg, *args, **kwargs):
    """Debug."""
    logger.debug(f"[trace_id={self._log_id}]||" + msg, *args, **kwargs)

  def info(self, msg, *args, **kwargs):
    """Info."""
    logger.info(f"[trace_id={self._log_id}]||" + msg, *args, **kwargs)

  def warning(self, msg, *args, **kwargs):
    """Warning."""
    logger.warning(f"[trace_id={self._log_id}]||" + msg, *args, **kwargs)

  def warn(self, msg, *args, **kwargs):
    """Warn will not output trace id."""
    print(self._log_id)
    logger.warning(msg, *args, **kwargs)

  def error(self, msg, *args, **kwargs):
    """Error."""
    logger.error(f"[trace_id={self._log_id}]||" + msg, *args, **kwargs)

  def critical(self, msg, *args, **kwargs):
    """Critical."""
    logger.critical(f"[trace_id={self._log_id}]||" + msg, *args, **kwargs)

  def monitor(self, msg, *args, **kwargs):
    """Monitor."""
    logger.monitor(f"[trace_id={self._log_id}]||" + msg, *args, **kwargs)

  def public(self, log_key, msg, *args, **kwargs):
    """Public."""
    logger.public(f"{log_key}||trace_id={self._log_id}||" + msg, *args,
                  **kwargs)


class ObjectWithTrace(ObjectWithlog):
  """Log with trace."""
  def __init__(self, trace: Trace) -> None:
    assert trace is not None, "trace is None."
    self._trace = trace
    super().__init__(self._trace.trace())

  @property
  def trace(self):
    """_trace."""
    return self._trace


class JobConf(ObjectWithlog):
  """Config of job."""
  def __init__(self,
               city_id: int = 0,
               map_region: str = "",
               strategy_names: List[str] = None,
               tid: str = None,
               mini_run: bool = False,
               run_imediately: bool = False,
               test_flag: bool = False):
    super().__init__()
    if strategy_names is None:
      strategy_names = []
    self.city_id: int = city_id
    self.map_region: str = map_region
    self.strategy_names_ori: List[str] = strategy_names
    self.tid: str = tid.strip() if tid is not None else None
    self.mini_run: bool = mini_run
    self.run_imediately: bool = run_imediately
    self.test_flag: bool = test_flag

  @property
  def id(self):
    """Combine an id from parameters."""
    return (f"city={self.city_id:d}-region={self.map_region}-tid={self.tid}"
            f"-mini_run={self.mini_run}-run_im={self.run_imediately}"
            f"-test={self.test_flag}-stgs={'|'.join(self.strategy_names_ori)}")

  def tid_valid(self):
    """Check tid valid."""
    return (self.tid is not None) and (len(self.tid) > 0) and (len(
        self.tid) == 11)


class EnvConfig(object):
  """Some environment Config."""
  def __init__(self,
               run_mode: RunMode = RunMode.PRODUCTION,
               mini_run: bool = False,
               run_imediately: bool = False) -> None:
    self.run_mode: RunMode = run_mode
    self.mini_run: bool = mini_run
    self.run_imediately: bool = run_imediately

  def read_test(self):
    """If get data from an offline environment database."""
    if self.run_mode == RunMode.DEV:
      return True
    return False

  def write_test(self):
    """If set data to an offline environment database."""
    if self.run_mode == RunMode.PRODUCTION:
      return False
    return True

  def env(self):
    """Env string."""
    return f"{self.run_mode}-{self.mini_run}-{self.run_imediately}"


class StrategyStatusCode(Enum):
  """The enum of starategy status."""
  Unknown = -1
  Success = 0
  GetDataError = 1
  ComputeError = 2
  SetDataError = 3
  OtherError = 4
  ValidateError = 5
