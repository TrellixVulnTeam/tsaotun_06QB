import sys

class Logger(object):
    """Logger class"""

    # Color codes
    STD = "\033[0;0m"
    BLUE = "\033[1;34m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"

    def __init__(self):
        pass

    @classmethod
    def log(self, fmt_string, *args):
        if len(args) == 0:
            print(fmt_string)
        else:
            print(fmt_string.format(*args))
        sys.stdout.write(self.STD)

    @classmethod
    def logInfo(self, fmt_string, *args):
        sys.stdout.write(self.BLUE)
        self.log(fmt_string, *args)
        

    @classmethod
    def logWarning(self, fmt_string, *args):
        sys.stdout.write(self.YELLOW)
        self.log(fmt_string, *args)
        

    @classmethod
    def logError(self, fmt_string, *args):
        sys.stdout.write(self.RED)
        self.log(fmt_string, *args)
        

    @classmethod
    def logSuccess(self, fmt_string, *args):
        sys.stdout.write(self.GREEN)
        self.log(fmt_string, *args)
        

    @classmethod
    def logProgressInfo(self, fmt_string, *args):
        sys.stdout.write(self.BLUE)
        if len(args) == 0:
            sys.stdout.write(fmt_string)
        else:
            sys.stdout.write(fmt_string.format(*args))
        sys.stdout.write(self.STD)
