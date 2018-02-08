from core.logging import *

def test_logging():
    log("default log test")
    log("error log test","ERROR")
    log("info log test","INFO")
    log("warning log test","WARNING")