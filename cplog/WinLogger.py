class WinLogger(object):
    def __init__(self):
        pass

    def closelog(self):
        pass

    def openlog(self):
        pass

    def echo_to_screen(self, flag):
        pass

    def set_loglevel(self, newlevel):
        pass

    def _int_to_level(self, priority):
        pass

    def log(self, message, priority):
        print message, priority
