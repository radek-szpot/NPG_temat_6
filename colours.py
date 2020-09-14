#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
A module that allows you to write colored texts
'''

def prRed(skk): print("\033[91m {}\033[00m" .format(skk), end='')
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk), end='')
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk), end='')