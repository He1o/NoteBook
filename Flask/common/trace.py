"""Trace class."""
import socket
import time
import uuid


class Trace(object):
  """Trace defines some unique parameters to represent identity."""
  def __init__(self, trace_name: str = "") -> None:
    self.trace_name = trace_name
    self.init_timestamp = int(time.time() * 1000)
    self.host = socket.gethostname()
    self.uuid = uuid.uuid4()

  def trace(self):
    """Generate unique identity."""
    if self.trace_name is None or len(self.trace_name.strip()) < 1:
      return f"{self.init_timestamp}-{self.host}-{self.uuid}"
    return (f"{self.trace_name}-"
            f"{self.init_timestamp}-"
            f"{self.host}-{self.uuid}")
