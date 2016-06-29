#!/usr/bin/env python2

import sys
import time

while True:
	text = raw_input()
	print text
	sys.stdout.flush()

	time.sleep(0.1)
