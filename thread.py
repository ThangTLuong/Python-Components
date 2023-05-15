import threading

class thread(threading.Thread):
  def __init__(self, group: None = None, target: None = None, name: str | None = None, args = ..., kwargs = {}) -> None:
    threading.Thread.__init__(self, group, target, name, args, kwargs)
    self._return = None

  def run(self):
    if self._target is not None:
      self._return = self._target(*self._args, **self._kwargs)

  def join(self):
    threading.Thread.join(self)
    return self._return
