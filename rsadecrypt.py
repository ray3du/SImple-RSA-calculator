#!/usr/bin/env python
import sys
import os
from time import sleep

key  = ""

if len(sys.argv) <= 2:
	print("Usage: ")
	print("python rsadecrypt.py <numeric file> <modulus> <d>")
else:
	file = sys.argv[1]
	modulus = sys.argv[2]
	d = sys.argv[3]
	f = open(file).read().split(" ")
	output = open("decrypted.rsa", "w")
	for line  in f:
		decrypted = (int(line)**int(d)) % int(modulus)
		key += chr(decrypted)
		print(key)

	os.system("clear")
	print("Writing to file decrypted.rsa..")
	sleep(2)
	output.write(key)
	print("Complete")