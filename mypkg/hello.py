#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tools.printf import printf


def say_hello(s):
    printf("Hello %s" % s, color="red")
    printf("Hello %s" % s, color="green")
    printf("Hello %s" % s, color="yellow")
    printf("Hello %s" % s, color="blue")

