"""Some logger classes inherit from logging.logger."""
# pylint: disable=W0703,W0212
import datetime
import logging
import os
import threading
import time
from typing import List
from logging.handlers import HTTPHandler, TimedRotatingFileHandler  # pylint: disable=C0412
from queue import Queue, Empty
from stat import ST_MTIME

K_LOGGING_PUBILC_LEVEL = 60
K_LOGGING_PUBILC_LEVEL_NAME = "PUBLIC"

K_LOGGING_MONITOR_LEVEL = 70
K_LOGGING_MONITOR_LEVEL_NAME = "MONITOR"


def Name2level(level_name: str) -> int:
  """Gets level by name."""
  _level_name = level_name.strip().upper()
  assert _level_name in logging._nameToLevel, \
         f"level [{_level_name}] not exists."
  return logging._nameToLevel[_level_name]


class VoyLogger(logging.Logger, object):
  """VoyLogger inherit from logging.
     Logger can support public and monitor levels."""
  def __init__(self, name: str, level: int = logging.NOTSET) -> None:
    super().__init__(name, level)
    logging.addLevelName(
        level=K_LOGGING_PUBILC_LEVEL, levelName=K_LOGGING_PUBILC_LEVEL_NAME)

  def public(self, msg, *args, **kwargs):
    """
    Log 'msg % args' with severity 'PUBLIC'.

    To pass exception information, use the keyword argument exc_info with
    a true value, e.g.

    logger.info("Houston, we have a %s", "interesting problem", exc_info=1)
    """
    if self.isEnabledFor(K_LOGGING_PUBILC_LEVEL):
      self._log(K_LOGGING_PUBILC_LEVEL, msg, args, **kwargs)

  def monitor(self, msg, *args, **kwargs):
    """
    Log 'msg % args' with severity 'MONITOR'.

    To pass exception information, use the keyword argument exc_info with
    a true value, e.g.

    logger.info("Houston, we have a %s", "interesting problem", exc_info=1)
    """
    if self.isEnabledFor(K_LOGGING_MONITOR_LEVEL):
      self._log(K_LOGGING_MONITOR_LEVEL, msg, args, **kwargs)


class VoyQueueListener(object):
  """Queue for remote log."""
  _sentinel = None

  def __init__(self, queue: Queue, handlers: List[logging.Handler]) -> None:
    self.queue = queue
    self.handlers = handlers
    self._threads = {}
    self.start()

  def dequeue(self, block):
    """
    Dequeue a record and return it, optionally blocking.

    The base implementation uses get. You may want to override this method
    if you want to use timeouts or work with custom queue implementations.
    """
    return self.queue.get(block)

  def start(self):
    """
    Start the listener.

    This starts up a background thread to monitor the queue for
    LogRecords to process.
    """
    for idx in range(len(self.handlers)):
      handler = self.handlers[idx]
      t = threading.Thread(target=self._monitor, args=(handler,))
      t.daemon = True
      t.start()
      self._threads[t] = f"{handler.get_name()}_{idx}"

  def prepare(self, record):  # pylint: disable=R0201
    """
    Prepare a record for handling.

    This method just returns the passed-in record. You may want to
    override this method if you need to do any custom marshalling or
    manipulation of the record before passing it to the handlers.
    """
    return record

  def _monitor(self, handler: logging.Handler):
    """Monitor."""
    q = self.queue
    has_task_done = hasattr(q, 'task_done')
    while True:
      try:
        record = self.dequeue(True)
        if record is self._sentinel:
          break
        record = self.prepare(record)
        handler.handle(record)
        if has_task_done:
          q.task_done()
      except Empty:
        break

  def enqueue_sentinel(self):
    """
    This is used to enqueue the sentinel record.

    The base implementation uses put_nowait. You may want to override this
    method if you want to use timeouts or work with custom queue
    implementations.
    """
    self.queue.put_nowait(self._sentinel)

  def stop(self):
    """
    Stop the listener.

    This asks the thread to terminate, and then waits for it to do so.
    Note that if you don't call this before your application exits, there
    may be some records still left on the queue, which won't be processed.
    """
    for thread in self._theads:
      if thread.isAlive():
        self.enqueue_sentinel()
        thread.join()
      else:
        print(f"thread {self._theads[thread]} closed.")


class LevelFilter(logging.Filter):
  """Filter level."""
  def __init__(self, rule):
    assert callable(rule), f"rule not callable, rule={rule}"
    self.rule = rule
    super().__init__("")

  def filter(self, record: logging.LogRecord):
    """Filter."""
    return self.rule(record.levelno)


class VoyRotatingFileHandler(TimedRotatingFileHandler):
  """A handler inherit from TimedRotatingFileHandler and change the start
  rollover time."""
  def __init__(self,
               filename: str,
               when: str = 'h',
               interval: int = 1,
               backupCount: int = 0,
               encoding: str = None,
               delay: bool = False,
               utc: bool = False,
               atTime: datetime.datetime = None) -> None:
    super().__init__(filename, when, interval, backupCount, encoding, delay,
                     utc, atTime)
    self.rolloverAt = self.InitrolloverAt()

  def InitrolloverAt(self) -> int:
    """
    Work out the rollover time based on the specified time.
    """

    filename = self.baseFilename
    if os.path.exists(filename):
      currentTime = os.stat(filename)[ST_MTIME]
    else:
      currentTime = int(time.time())

    if self.when == 'MIDNIGHT' or self.when.startswith('W'):
      return self.rolloverAt
    else:
      currentTime_new = currentTime - currentTime % self.interval
      print(f"t_ori={currentTime}, currentTime_new={currentTime_new}, " +
            f"interval={self.interval}")
      result = currentTime_new + self.interval
    return result


class VoyRotatingFileHandlerV2(TimedRotatingFileHandler):
  """Modifies the log file's name to with a date as sufix."""
  def __init__(self,
               filename: str,
               when: str = 'H',
               interval: int = 1,
               backupCount: int = 5,
               encoding: str = None,
               delay: bool = False,
               utc: bool = False,
               atTime: datetime.datetime = None) -> None:

    self._currentFileName = None
    super().__init__(filename, when, interval, backupCount, encoding, delay,
                     utc, atTime)
    self._currentFileName = self.CurrentFileName()
    self.rolloverAt = self.InitrolloverAt()

  def CurrentFileName(self):
    """Gets file name based on current time."""
    currentTime = int(time.time())
    if self.utc:
      timeTuple = time.gmtime(currentTime)
    else:
      timeTuple = time.localtime(currentTime)
    return self.rotation_filename(
        self.baseFilename + "." + time.strftime(self.suffix, timeTuple))

  def _open(self):
    """Opens or creates log."""
    if self._currentFileName is not None:
      self._currentFileName = self.CurrentFileName()
      return open(self._currentFileName, self.mode, encoding=self.encoding)
    return open(self.baseFilename, self.mode, encoding=self.encoding)

  def InitrolloverAt(self) -> int:
    """
        Work out the rollover time based on the specified time.
        """
    if self.stream:
      self.stream.close()
      if os.path.exists(self.baseFilename):
        os.remove(self.baseFilename)
      if not self.delay:
        self.stream = self._open()
    filename = self._currentFileName
    if os.path.exists(filename):
      createTime = os.stat(filename)[ST_MTIME]
    else:
      createTime = int(time.time())

    if self.when == 'MIDNIGHT' or self.when.startswith('W'):
      return self.rolloverAt
    else:
      createTime_new = createTime - createTime % self.interval
      print(f"t_ori={createTime}, currentTime_new={createTime_new}, " +
            f"interval={self.interval}")
      result = createTime_new + self.interval
    return result

  def doRollover(self):
    """
    do a rollover; in this case, a date/time stamp is appended to the filename
    when the rollover happens.  However, you want the file to be named for the
    start of the interval, not the current time.  If there is a backup count,
    then we have to get a list of matching filenames, sort them and remove
    the one with the oldest suffix.
    """
    if self.stream:
      self.stream.close()
      self.stream = None
    # get the time that this sequence started at and make it a TimeTuple
    currentTime = int(time.time())
    dstNow = time.localtime(currentTime)[-1]
    if self.backupCount > 0:
      for s in self.getFilesToDelete():
        os.remove(s)
    if not self.delay:
      self.stream = self._open()
    newRolloverAt = self.computeRollover(currentTime)
    while newRolloverAt <= currentTime:
      newRolloverAt = newRolloverAt + self.interval
    # If DST changes and midnight or weekly rollover, adjust for this.
    if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
      dstAtRollover = time.localtime(newRolloverAt)[-1]
      if dstNow != dstAtRollover:
        # DST kicks in before next rollover, so we need to deduct an hour
        if not dstNow:
          addend = -3600
        else:  # DST bows out before next rollover, so we need to add an hour
          addend = 3600
        newRolloverAt += addend
    self.rolloverAt = newRolloverAt


class VoyHTTPHandler(HTTPHandler):
  """This handles will send log message to remote server."""
  def __init__(self,
               host: str,
               url: str,
               method: str = "POST",
               secure=False,
               credentials=None,
               context=None) -> None:
    super().__init__(host, url, method, secure, credentials, context)

  def mapLogRecord(self, record: logging.LogRecord):
    """
        Default implementation of mapping the log record into a dict
        that is sent as the CGI data. Overwrite in your class.
        Contributed by Franz Glasner.
        """
    return {f"{record.levelname}": [self.format(record=record)]}

  def emit(self, record):
    """
        Emit a record.

        Send the record to the Web server as a percent-encoded dictionary
        """
    try:
      import http.client
      import urllib.parse
      host = self.host
      if self.secure:
        h = http.client.HTTPSConnection(host, context=self.context)
      else:
        h = http.client.HTTPConnection(host)
      url = self.url
      data = urllib.parse.urlencode({"log": self.mapLogRecord(record)})

      if self.method == "GET":
        if url.find('?') >= 0:
          sep = '&'
        else:
          sep = '?'
        url = url + "%c%s" % (sep, data)
      h.putrequest(self.method, url)
      # support multiple hosts on one IP address...
      # need to strip optional :port from host, if present
      i = host.find(":")
      if i >= 0:
        host = host[:i]
      # See issue #30904: putrequest call above already adds this header
      # on Python 3.x.
      # h.putheader("Host", host)
      if self.method == "POST":
        h.putheader("Content-type", "application/x-www-form-urlencoded")
        h.putheader("Content-length", str(len(data)))
      if self.credentials:
        import base64
        s = ('%s:%s' % self.credentials).encode('utf-8')
        s = 'Basic ' + base64.b64encode(s).strip().decode('ascii')
        h.putheader('Authorization', s)
      h.endheaders()
      if self.method == "POST":
        h.send(data.encode('utf-8'))
      h.getresponse()  # can't do anything with the result
    except Exception:
      self.handleError(record)
