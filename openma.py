from test.test_color import *
from test.test_config import *
from test.test_now import *
from test.test_logging import *
from test.test_virtualbox import *
from test.test_db import  *
from test.test_sniffer import *

if __name__ == '__main__':
    test_color()
    test_config()
    test_now()
    test_logging()
    test_virtualbox()
    test_db()
    test_sniffer()
