"""Define strategy item and manager."""
import abc
from typing import (Callable, List, Dict)

from Flask.common.common import JobConf
from Flask.common.log_tools import logger
from Flask.common.trace import Trace


def init():
  """Init global strategy manager."""
  global strategy_manager  # pylint: disable=W0601
  strategy_manager = StrategyManager()
  return strategy_manager


class StrategyBase:
  """The basic class of strategy."""
  @abc.abstractclassmethod
  def reset(cls, job_conf: JobConf, trace: Trace) -> bool:
    """Reset."""
    pass

  @abc.abstractclassmethod
  def execute_list(cls) -> List[Callable]:
    """Execute list."""
    pass


class StrategyItem(object):
  """Defines strategy's name and method."""
  def __init__(self, name: str, generator):
    assert callable(generator), "generator invalid."
    self.__name = name
    self.__generator = generator

  @property
  def name(self):
    """Name."""
    return self.__name

  @property
  def generator(self):
    """Generate is a class include the specific stragety."""
    return self.__generator

  def id(self):
    """Unique id."""
    info = f"name={self.__name},"
    info += f"strategy={self.__generator()}"
    return info


class StrategyManager(object):
  """Strategy manager will managers all the strategyItems."""
  def __init__(self):
    self.__name2strategy: Dict[str, StrategyItem] = {}

  def register_strategy(self, name: str, generator) -> bool:
    """Add a strategy."""
    if name not in self.__name2strategy:
      self.__name2strategy[name] = StrategyItem(name=name, generator=generator)
      logger.info(f"register_strategy succ, name={name}")
      return True
    logger.error(f"register_strategy error, strategy {name} exists")
    return False

  def get_all_strategy_names(self) -> List[str]:
    """Return all the strategies' names."""
    return list(self.__name2strategy.keys)

  def get_strategy_by_name(self, name: str) -> StrategyBase:
    """Get strategy by name."""
    if name not in self.__name2strategy:
      return None
    return self.__name2strategy[name].generator()

  @staticmethod
  def get_instance():
    """Get global strategy manager."""
    return strategy_manager
