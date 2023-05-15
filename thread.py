import threading
import typing

class thread(threading.Thread):
  
  _return_data = None
  
  #==============================================================================#
  def __init__(self, group: None = None, target: None = None, name: str | None = None, args = ..., kwargs = {}, enable: bool = False) -> None:
    threading.Thread.__init__(self, group, target, name, args, kwargs)
    self._return_data = enable
    if self._return_data:
      self._return = None
  
  #==============================================================================#

  #==============================================================================#
  def run(self) -> None:
    try:
      if self._target is not None:
        if self._return_data:
          self._return = self._target(*self._args, **self._kwargs)
        else:
          self._target(*self._args, **self._kwargs)
    finally:
      # Avoid a refcycle if the thread is running a function with
      # an argument that has a member that points to the thread.
      del self._target, self._args, self._kwargs
  
  #==============================================================================#

  #==============================================================================#
  def join(self) -> typing.Union[any, None]:
    threading.Thread.join(self)
    if self._return_data:
      return self._return
  
  #==============================================================================#