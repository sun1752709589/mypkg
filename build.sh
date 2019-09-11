#!/usr/bin/env bash
# !/bin/sh

echo off
echo building...
python setup.py build_ext --inplace
echo build end

echo publishing...
python setup.py sdist
echo publish end