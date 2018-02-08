import time
import datetime

from core.config import *

def get_now(format = "%Y-%m-%d %H:%M:%S"):
    # According to configuration, choose between UTC time and local time.
    if OpenMAConfig().get_logging_utc() == "True":
        time = datetime.datetime.utcnow()
    else:
        time = datetime.datetime.now()

    now = time.strftime(format)
    
    return now
