"""Error code and message."""


class Error(object):
  """Error class include error message and error code."""
  def __init__(self, code: int = 0, msg: str = "") -> None:
    self.__code = code
    self.__msg = msg

  @property
  def code(self) -> int:
    """Error code."""
    return self.__code

  @property
  def msg(self):
    """Error message."""
    return self.__msg

  @property
  def str_info(self):
    """Consists of error message and error code."""
    info = ""
    info += f"[code={self.__code}, "
    info += f"msg={self.__msg}]"
    return info
