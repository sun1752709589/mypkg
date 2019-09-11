#!/usr/bin/env python
# -*- coding: utf-8 -*-


def printf(s, color="red"):
    if color == "red":
        print("\033[0;31m%s\033[0m" % s)
    elif color == "green":
        print("\033[0;32m%s\033[0m" % s)
    elif color == "yellow":
        print("\033[0;33m%s\033[0m" % s)
    elif color == "blue":
        print("\033[0;34m%s\033[0m" % s)
    elif color == "white":
        print("\033[0;37m%s\033[0m" % s)
    else:
        print(s)


if __name__ == '__main__':
    printf("Hello", color="green")
