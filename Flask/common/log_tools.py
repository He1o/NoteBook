"""Log tools defines a global logger."""
import logging
import os
from typing import List
from queue import Queue

from Flask.common import constant
from Flask.common import logger_base
from Flask.common.context import context

logging.setLoggerClass(logger_base.VoyLogger)
logger = logging.getLogger('prior_map_cloud')
_queue = Queue(maxsize=10000)


def getLogQueue():
  """Gets queue."""
  return _queue


# ADD LEVEL
def init_logging(level: int = None,
                 logging_format: str = None,
                 use_http_handler: bool = None,
                 save_to_file: bool = None,
                 **kwargs):
  """Just need to initialize the logging once,
  then logger can be useeds anywhere."""
  if level is None:
    level = constant.K_LOGGING_LEVEL
  if logging_format is None:
    logging_format = constant.K_LOGGING_FORMAT
  logging.setLoggerClass(logger_base.VoyLogger)
  logging.basicConfig(level=level, format=logging_format, **kwargs)
  logging.addLevelName(
      level=logger_base.K_LOGGING_PUBILC_LEVEL,
      levelName=logger_base.K_LOGGING_PUBILC_LEVEL_NAME)
  logging.addLevelName(
      level=logger_base.K_LOGGING_MONITOR_LEVEL,
      levelName=logger_base.K_LOGGING_MONITOR_LEVEL_NAME)
  _init_logger(use_http_handler=use_http_handler, save_to_file=save_to_file)


def _init_logger(use_http_handler: bool = None,
                 save_to_file: bool = None) -> logger_base.VoyLogger:
  """Inner function to initialize the logger."""
  # voy_logger = logging.getLogger(name)
  if use_http_handler is None:
    use_http_handler = constant.K_HTTP_HANDLER
  if save_to_file is None:
    save_to_file = constant.K_LOGGING_SAVE_LOCAL
  if use_http_handler:
    logger.addHandler(getHttpHandler())
  if save_to_file:
    file_handlers = getFileHandlers(constant.K_LOGGING_DIR, need_rotation=True)
    for handler in file_handlers:
      logger.addHandler(handler)
  return logger


def getFileHandlers(log_dir: str,
                    need_rotation: bool = False) -> List[logging.Handler]:
  """Set handles."""
  if not os.path.exists(log_dir):
    os.system(f"mkdir -p {log_dir}")
  log_path_info = f"{log_dir}/access.log.info"
  log_path_wf = f"{log_dir}/access.log.wf"
  log_path_public = f"{log_dir}/public.log"
  log_path_monitor = f"{log_dir}/access.log.monitor"
  info_handler = logging.FileHandler(
      filename=log_path_info, encoding='UTF-8'
  ) if not need_rotation else logger_base.VoyRotatingFileHandlerV2(
      filename=log_path_info, encoding='UTF-8')
  info_handler.setFormatter(logging.Formatter(constant.K_LOGGING_FORMAT))
  info_handler.addFilter(
      logger_base.LevelFilter(
          rule=lambda x: (logging.DEBUG <= x <= logging.INFO)))

  wf_handler = logging.FileHandler(
      filename=log_path_wf, encoding='UTF-8'
  ) if not need_rotation else logger_base.VoyRotatingFileHandlerV2(
      filename=log_path_wf, encoding='UTF-8')
  wf_handler.setFormatter(logging.Formatter(constant.K_LOGGING_FORMAT))
  wf_handler.addFilter(
      logger_base.LevelFilter(
          rule=lambda x: (logging.WARNING <= x <= logging.CRITICAL)))

  public_handler = logging.FileHandler(
      filename=log_path_public, encoding='UTF-8'
  ) if not need_rotation else logger_base.VoyRotatingFileHandlerV2(
      filename=log_path_public, encoding='UTF-8')
  public_handler.setFormatter(logging.Formatter(constant.K_LOGGING_FORMAT))
  public_handler.addFilter(
      logger_base.LevelFilter(
          rule=lambda x: (x == logger_base.K_LOGGING_PUBILC_LEVEL)))

  monitor_handler = logging.FileHandler(
      filename=log_path_monitor, encoding='UTF-8'
  ) if not need_rotation else logger_base.VoyRotatingFileHandlerV2(
      filename=log_path_monitor, encoding='UTF-8')
  monitor_handler.setFormatter(logging.Formatter(constant.K_LOGGING_FORMAT))
  monitor_handler.addFilter(
      logger_base.LevelFilter(
          rule=lambda x: (x == logger_base.K_LOGGING_MONITOR_LEVEL)))

  return [info_handler, wf_handler, public_handler, monitor_handler]


def getHttpHandler(host: str = None,
                   url: str = None,
                   method: str = None,
                   levels: List[int] = [
                       logging.WARNING, logging.ERROR, logging.CRITICAL,
                       logger_base.K_LOGGING_MONITOR_LEVEL
                   ]):  # pylint: disable=W0102
  """Generates HttpHandles."""
  if host is None:
    host = constant.K_HTTP_HANDLER_HOST[context.env_key()]
  if url is None:
    url = constant.K_HTTP_HANDLER_URL
  if method is None:
    method = constant.K_HTTP_HANDLER_METHOD
  print(f"host={host}, url={url}, method={method}, levels={levels}")
  http_handler = logger_base.VoyHTTPHandler(host=host, url=url, method=method)
  http_handler.setFormatter(logging.Formatter(constant.K_LOGGING_FORMAT))
  if levels is not None:
    http_handler.addFilter(logger_base.LevelFilter(lambda x: x in levels))
  return http_handler
