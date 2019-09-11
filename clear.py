#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

PYTHON3 = sys.version_info >= (3,)
ROOT_PATH = os.path.abspath(os.path.dirname(__name__))

for (path, dirs, files) in os.walk(ROOT_PATH):
    for filename in files:
        # if (path.find("__pycache__") >= 0 or path.find(".git") >= 0) and os.path.exists(path):
        #     print("deleting {0}..".format(path))
        #     shutil.rmtree(path)
        (shotname, extension) = os.path.splitext(filename)
        if extension == ".so" or extension == ".pyc" or extension == ".pyd" or extension == ".c":
            file_path = os.path.abspath(os.path.join(path, filename))
            os.remove(file_path)
            print("deleting {0}..".format(file_path))
