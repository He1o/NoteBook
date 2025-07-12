"""Provide a function to get server type whitch is based on host name."""
import socket
from Flask.common.constant import K_HOST_ENV, K_PRODUCTION, K_PRE
from Flask.common.context import RunMode


def get_host_env():
  """Get server type depends on host name."""
  host_name = socket.gethostname()
  run_mode = RunMode.DEV
  if host_name in K_HOST_ENV:
    host_env = K_HOST_ENV[host_name]
    if host_env == K_PRODUCTION:
      run_mode = RunMode.PRODUCTION
    elif host_env == K_PRE:
      run_mode = RunMode.PRE
  return run_mode
