import sys

if sys.platform.startswith('linux'):
    from UnixLogger import UnixLogger
    _logger = UnixLogger()
else:
    from WinLogger import WinLogger
    _logger = WinLogger()

# Priorities
internal = 5
verbose = 4
debug = 3
notice = 2
warning = 1
error = 0

def log(message, priority=notice):
    _logger.log(message, priority)

def closelog():
    _logger.closelog()

def openlog():
    _logger.openlog()

def set_loglevel(newlevel):
    _logger.set_loglevel(newlevel)

def echo_to_screen(flag):
    _logger.echo_to_screen(flag)
