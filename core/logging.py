import os
import sys

from core.now import *
from core.color import *
from core.config import *

def log(message, level = "DEFAULT"):
    log_file = OpenMAConfig().get_logging_path()
    level = level.upper()

    # If log level is "DEBUG", than just print message on screen.
    if level == "DEBUG":
         if OpenMAConfig().get_logging_debug() == "True":
             line = "[%s] [DEBUG] %s\n" % (get_now(), message)
             sys.stdout.write(line)
    # Otherwise log message on file.
    else:
        if level == "WARNING" or level == "ERROR":
            line = "[%s] [%s] %s\n" % (get_now(), level, message)
        else:
            line = "[%s] %s\n" % (get_now(), message)

        if os.path.exists(log_file):
            log = open(log_file, "a")
        else:
            log = open(log_file, "w")

        try:
            #line = unicode(line, "utf-8").encode("utf-8")
            log.write(line)
            log.close()

            if level == "WARNING":
                sys.stdout.write(yellow(line))
            elif level == "ERROR":
                sys.stdout.write(bold(red(line)))
            elif level == "INFO":
                sys.stdout.write(cyan(line))
            else:
                sys.stdout.write(line)
        except Exception, why:
            sys.stdout.write(yellow("Unable to log event: %s" % why))

    return
