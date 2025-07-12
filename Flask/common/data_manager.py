"""A DataManage to manage database accesses."""
from concurrent.futures import (Future, ThreadPoolExecutor, as_completed)
from typing import (Callable, Dict, Tuple)

from Flask.common.common import (ObjectWithTrace)
from Flask.common.context import context

class DataManager(ObjectWithTrace):
  """Manage all process about database."""

  def __init__(self, thread_pool_size: int, trace):
    super().__init__(trace=trace)
    self._thread_pool_size = thread_pool_size
    self._thread_pool = ThreadPoolExecutor(self._thread_pool_size)
    self.__init_accesses()

  def __init_accesses(self):
    """Init all database accesses."""
    pass

  def do(self):
    """Handles all database related processes."""
    pass

  @property
  def str(self):
    """Str."""
    return self.__str__

