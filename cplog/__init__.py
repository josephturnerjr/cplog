import sys
from UnixLogger import UnixLogger
from WinLogger import WinLogger

if sys.platform.startswith('linux'):
    _logger = UnixLogger()
else:
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
