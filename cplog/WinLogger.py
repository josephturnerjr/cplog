class WinLogger(object):
    def __init__(self):
        self.loglevel = 0
        self.log_filename = r"C:\log.txt"
        self.echo = False

    def closelog(self):
        pass
        
    def openlog(self):
        pass
    
    def set_log_filename(self, filename):
        self.log_filename = filename

    def echo_to_screen(self, flag):
        self.echo = True

    def set_loglevel(self, newlevel):
        self.loglevel = newlevel

    def log(self, message, priority):
        if priority <= self.loglevel:
            if self.log_filename:
                try:
                    with open(self.log_filename, "a") as log:
                        log.write(message)
                except IOError, e:
                    print "Couldn't open logfile %s: %s" % (self.log_filename, 
                                                            e)
            if self.echo:
                print message
            
