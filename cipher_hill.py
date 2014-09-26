# coding: utf-8

"""
author: Guilherme Carvalho
date: 	25 Sep 2014
title:	cipher_hill.py
"""

import sys 
import string
import numpy

def convert_letters_number_range(letters):
	"""
	convert_letters_number_range(...)
	convert_letters_number_range(letters) -> list[integer] -- returns a list with ordinal numbers of each letters of string passed by parameter
	"""
	letters_converted = []
	
	for l in letters:
		n = (ord(l) - 65) % 26
		letters_converted.append([n])

	return letters_converted

def slicen(string, interval=2):
	"""
	slicen(...)
	slicen(string, interval=2) -> string -- returns the string in chuncks of size indicated by interval, interval by default is two.
	"""
	# counter indicates the last stop
	i = 0 

	while len(string) > i:
		# returns a chunk of string, begins by i going until n more i 
		yield string[i:(i+interval)]
		i += interval

def crypt(msg, mkey, interval):
	"""
	crypt(...)
	crypt(msg, alphabet, mkey) -> string -- return encrypted string
	"""
	alphabet = string.letters
	encrypted_string = []

	# returns the number rows and columns of matrix
	nrows, ncolumns = mkey.shape

	for chunk in slicen(msg, interval):
		mletters = convert_letters_number_range(chunk)
		try:
			numpy.matrix(mletters)
			m = mkey * mletters
			m = m.tolist()
			encrypted_string += map(lambda i: alphabet[i%26], [m[0][0], m[1][0]])
		except ValueError as e:
			print e

	return ''.join(encrypted_string)

def decrypt(msg, mkey, interval):
	"""
	decrypt(...)
	decrypt(msg, mkey, interval) -> string -- return decrypted string
	"""
	print mkey
	print mkey.I


def main():
	mkey = numpy.matrix([[3, 2], [5, 7]])

	if len(sys.argv) < 2:
		sys.exit('[ERROR]: Invalid type, enter with text to encrypt.')

	msg = sys.argv[1]
	msg = msg.upper()

	# decrypt(msg, mkey, 2)

	print crypt(msg, mkey, 2).upper()

if __name__ == '__main__':
	main()