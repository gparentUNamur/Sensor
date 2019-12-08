import threading


class TaskThread(threading.Thread):
    def __init__(self, interval=15.0):
        threading.Thread.__init__(self)
        self._finished = threading.Event()
        self._interval = interval

    def set_interval(self, interval):
        """Set the number of seconds we sleep between executing our task"""
        self._interval = interval

    def shutdown(self):
        """Stop this thread"""
        self._finished.set()

    def run(self):
        while 1:
            if self._finished.isSet():
                print("finished")
                return
            self.task()

            # sleep for interval or until shutdown
            self._finished.wait(self._interval)

    def task(self):
        """The task done by this thread - override in subclasses"""
        pass
