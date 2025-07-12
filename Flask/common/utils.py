"""Some common utils."""
# pylint: disable=W0703
import functools
import hashlib
import os
import time
from typing import (Any, Callable, Tuple)

from Flask.common.error import Error


def time_consume(func):
  """Records time consume."""

  def wrapper(*args, **kwargs):
    """Wrapper."""
    startTime = time.time()
    resp = func(*args, **kwargs)
    endTime = time.time()
    msecs = (endTime - startTime) * 1000
    print("time is %d ms" % msecs)
    return resp

  return wrapper


def get_timestamp(use_ms: bool = True):
  """Gets current timestamp"""
  current_time = time.time()
  if use_ms:
    return int(current_time * 1000)
  return int(current_time)


def get_dir(surfix: str):
  """Get current directory."""
  cwd = os.getcwd()
  parts = []
  finded = False
  for part in cwd.strip().split("/"):
    if part == surfix:
      parts.append(part)
      finded = True
      break
    else:
      parts.append(part)
  if finded:
    return "/".join(parts)
  return None


def get_func_name(func: Callable) -> str:
  """Gets function's name."""
  if isinstance(func, functools.partial):
    return func.func.__name__
  try:
    return func.__name__
  except Exception as e:
    print(f"get_func_name error,e={e}")
    return ""


def func_executor(fn: Callable, need_try_except, dm) -> Tuple[Error, int]:
  """Executes the function."""
  if need_try_except:
    try:
      return fn(dm)
    except Exception as e:
      print.error(f"func_executor error,e={e}")
      return Error(1, f"func={fn} exec error"), 0
  else:
    return fn(dm)


def get_md5(val: str) -> str:
  """md5."""
  return hashlib.md5(str(val).encode(encoding='UTF-8')).hexdigest()


def get_short_cut(val: Any, max_length: int = 20) -> bool:
  """Short cut the value."""
  val = str(val)
  return val[:max_length]
