import syslog


class UnixLogger(object):
    def __init__(self):
        self.set_loglevel(0)
        self.options = syslog.LOG_PID
        self.facility = syslog.LOG_DAEMON
        self.stderr = syslog.LOG_PERROR
        self.openlog()

    def closelog(self):
        syslog.closelog()
        
    def openlog(self):
        logopt = self.options|self.stderr
        # This is broken in the documentation! 
        # Documentation calls for a 'logopt' kwarg, but its actually logoption
        # See bug http://bugs.python.org/issue11648
        syslog.openlog(logoption=logopt, facility=self.facility)

    def echo_to_screen(self, flag):
        if flag:
            self.stderr = syslog.LOG_PERROR
        else:
            self.stderr = 0
        self.openlog()

    def set_loglevel(self, newlevel):
        l = self._int_to_level(newlevel)
        self.mask = syslog.LOG_UPTO(l)
        syslog.setlogmask(self.mask)

    def _int_to_level(self, loglevel):
        if loglevel == 0:
            l = syslog.LOG_ERR   
        elif loglevel == 1:
            l = syslog.LOG_WARNING
        elif loglevel == 2:
            l = syslog.LOG_NOTICE
        elif loglevel == 3:
            l = syslog.LOG_INFO
        elif loglevel >= 4:
            l = syslog.LOG_DEBUG
        return l

    def log(self, message, priority):
        syslog.syslog(self._int_to_level(priority), str(message))
