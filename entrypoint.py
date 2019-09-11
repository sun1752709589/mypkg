#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mypkg.hello import say_hello


def run():
    say_hello("Cython")


if __name__ == '__main__':
    run()
