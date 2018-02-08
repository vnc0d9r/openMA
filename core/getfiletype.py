import re
import os

from core.logging import *

def get_filetype(file_path):
    if not os.path.exists(file_path):
        log("[Get File Type] Cannot find file at path \"%s\"." % file_path,
            "ERROR")
        return None

    data = open(file_path, "rb").read()

    if re.match("MZ", data):
        return "exe"
    elif re.match("%PDF", data):
        return "pdf"
    else:
        return "Not supported"
