"""A global thread pool."""
from concurrent.futures import ThreadPoolExecutor


def init(thread_size: int = 20) -> ThreadPoolExecutor:
  """Init global thread pool."""
  global thread_pool  # pylint: disable=W0601
  thread_pool = ThreadPoolExecutor(max_workers=thread_size)
  return thread_pool


def get_thread_pool() -> ThreadPoolExecutor:
  """Gets global thread pool."""
  return thread_pool
