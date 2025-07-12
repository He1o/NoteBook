"""A global context include some info about environment.After init,the context
   can be used every where."""
from enum import Enum
import os
from Flask.common import constant
from Flask.common import utils


class RunMode(Enum):
  """Run Mode."""
  PRODUCTION = 0  # Read and write all on online environment.
  PRE = 1  # Read online,write offline.
  DEV = 2  # read and write all on offline environment.


class DirInfo(object):
  """Defines some environment directory."""
  def __init__(self,
               project_dir: str = "",
               build_dir: str = "",
               tmp_dir: str = "") -> None:
    self.project_dir: str = project_dir.strip()
    self.build_dir: str = build_dir.strip()
    self.tmp_dir = tmp_dir.strip()

  def reset(self, run_mode: RunMode = RunMode.PRODUCTION) -> bool:
    """Reset or init directories."""
    self.__init_project_dir(run_mode)
    self.__init_build_dir(run_mode)
    self.__init_tmp_dir(run_mode)
    return self.valid()

  def __init_project_dir(self, run_mode: RunMode = RunMode.PRODUCTION):
    """Init directories."""
    if self.project_dir:
      return
    if run_mode in [RunMode.PRODUCTION, RunMode.PRE]:
      self.project_dir = "/home/xiaoju/data1/voyager"
    elif run_mode == RunMode.DEV:
      self.project_dir = utils.get_dir("voyager")

  def __init_build_dir(self, run_mode: RunMode = RunMode.PRODUCTION):
    """Init build directory."""
    if self.build_dir:
      return
    if run_mode in [RunMode.PRODUCTION, RunMode.PRE]:
      self.build_dir = "/home/xiaoju/data1/build"
    elif run_mode == RunMode.DEV:
      self.build_dir = f"{self.project_dir}/../build"

  def __init_tmp_dir(self, run_mode: RunMode = RunMode.PRODUCTION):
    """Init temporary directory."""
    if self.tmp_dir:
      return
    if run_mode in [RunMode.PRODUCTION, RunMode.PRE]:
      self.tmp_dir = "/home/xiaoju/data1/tmp_z/"
    elif run_mode == RunMode.DEV:
      self.tmp_dir = f"{self.project_dir}/../tmp_z"

  def valid(self) -> bool:
    """Check if directories are exist."""
    if not os.path.exists(self.project_dir):
      return False
    if not os.path.exists(self.build_dir):
      return False
    if not os.path.exists(self.tmp_dir):
      os.mkdir(self.tmp_dir)
    return True

  def to_string(self):
    """String."""
    return f"{self.project_dir}_{self.build_dir}_{self.tmp_dir}"


class Context(object):
  """Context for runmode and dirInfo."""
  def __init__(self,
               project_dir: str = "",
               build_dir: str = "",
               tmp_dir: str = "",
               run_mode: RunMode = RunMode.PRODUCTION) -> None:
    self.dir_info = DirInfo(
        project_dir=project_dir, build_dir=build_dir, tmp_dir=tmp_dir)
    self.run_mode: RunMode = run_mode

  def init(self,
           project_dir: str = "",
           build_dir: str = "",
           tmp_dir: str = "",
           run_mode: RunMode = RunMode.PRODUCTION):
    """Init."""
    self.dir_info = DirInfo(
        project_dir=project_dir, build_dir=build_dir, tmp_dir=tmp_dir)
    self.run_mode: RunMode = run_mode
    assert self.dir_info.reset(
        self.run_mode
    ), f"dir_info not valid, dir_info={self.dir_info.to_string()}"

  def read_test(self) -> bool:
    """If get data from an offline environment database."""
    if self.run_mode == RunMode.DEV:
      return True
    return False

  def write_test(self) -> bool:
    """If set data to an offline environment database."""
    if self.run_mode == RunMode.PRODUCTION:
      return False
    return True

  def env(self):
    """Env string."""
    return f"{self.run_mode}"

  def product_env(self):
    """Check if is online environmnet."""
    return self.run_mode == RunMode.PRODUCTION

  def env_key(self):
    """Get run mode key."""
    key = constant.K_DEV
    if self.run_mode == RunMode.PRODUCTION:
      key = constant.K_PRODUCTION
    elif self.run_mode == RunMode.PRE:
      key = constant.K_PRE
    else:
      key = constant.K_DEV
    return key


context = Context()


def _init_context(project_dir: str = "",
                  build_dir: str = "",
                  tmp_dir: str = "",
                  run_mode: RunMode = RunMode.PRODUCTION):
  """Init global context."""
  global context  # pylint: disable=W0603
  context.init(
      project_dir=project_dir,
      build_dir=build_dir,
      tmp_dir=tmp_dir,
      run_mode=run_mode)
