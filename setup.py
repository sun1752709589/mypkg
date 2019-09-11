# -*- coding: utf-8 -*-

import os
import fileinput
import sys
from setuptools import setup, find_packages
from codecs import open
from Cython.Build import cythonize
from mypkg.version import __pkgname__, __version__

requires = []
require_file = 'requirements.txt'
if sys.platform.lower()[:3] == 'win':
    requires.append('pywin32>=219')
for line in fileinput.input(require_file):
    requires.append(line.replace('\n', ''))

packages = find_packages()

ext_modules = ['xxx.py'] # add what you want convert .c
# for (path, dirs, files) in os.walk("mypkg"):
#     for filename in files:
#         file = os.path.join(path, filename)
#         if '__init__' != os.path.splitext(filename)[0] and '.py' == os.path.splitext(filename)[1]:
#             ext_modules.append(file)

with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name=__pkgname__,
    version=__version__,
    author='laucyun<liu@laucyun.com>',
    author_email='',
    description='',
    long_description=history,
    url='-',
    packages=[],
    package_data={},
    include_package_data=True,
    scripts=['entrypoint.py'],
    entry_points={
        "console_scripts": ["%s=entrypoint:run" % __pkgname__]
    },
    package_dir={'mypkg': 'mypkg'},
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    ext_modules=cythonize(ext_modules),
)
