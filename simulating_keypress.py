#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'imita4i'

import enum
import time
import sys
from pynput.keyboard import Key, Controller

def press_key(key):
	# if isinstance(key, enum.Enum) | isinstance(key, str) & (len(key) == 1):
	if (key == "\n"): # win1251 is a trick of the devil
		return
	Controller().press(key)
	Controller().release(key)

def spell(filename):
	file = open(filename, 'r')
	for line in file.readlines():
		for character in line:
			press_key(character)
			time.sleep(0.075) 
		press_key(Key.enter)

def main() -> int:
	if (len(sys.argv) != 2):
		print(sys.argv[0] + " filename")
		return 1
	time.sleep(5)
	spell(sys.argv[1])
	return 0

if __name__ == '__main__':
	sys.exit(main())