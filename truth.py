#!/usr/bin/python

import re

in_string = raw_input("Enter boolean expression: ")
l_string = in_string

# find the variables (eliminate duplicates)
list = sorted(list(set(re.findall(r"\w+", in_string))))
num_rows = 2 ** len(list)

# replace boolean variables with array indices
for i in range(len(list)):
	# use negative lookahead and lookbehind to ensure exact string is replaced
	# e.g. abba & dabba case
	l_string = re.sub("(?<!\\w)" +list[i]+"(?!\\w)", "l["+str(i)+"]", l_string)
	print list[i] + " |",

print "out"

l = [False] * len(list)
for i in range(num_rows):
	# change variable values in compliance with counting order
	for j in range(len(l)):
		if ((i) % (2 ** (len(l)-1-j)) == 0) and i != 0:
			l[j] = not l[j]
	print "".join([str(int(l[k])) + " | " for k in range(len(l))])+ str(int(eval(l_string)) & 1)
