"""
Write a script to find duplicate files which have the same size and content.
"""

import hashlib
import os
import sys
from sets import Set

def read_chunk(fobj, chunk_size = 2048):
	""" Files can be huge so read them in chunks of bytes. """
	while True:
		chunk = fobj.read(chunk_size)
		if not chunk:
			return
		yield chunk

def find_duplicates(dir, hashfun = hashlib.sha512):
	unique = Set()
	for filename in os.listdir(dir):
		if filename.endswith(".txt"):
			filepath = os.path.join(dir, filename)
			if os.path.isfile(filepath):
				hashobj = hashfun()
				for chunk in read_chunk(open(filepath,'rb')):
					hashobj.update(chunk)
				hashfile = hashobj.hexdigest()
				if hashfile not in unique:
					unique.add(hashfile)
				else: 
					duplicateFIles.append(filepath)

if __name__=="__main__":
	duplicateFIles = []
	try:
		hashfun = hashlib.sha256
		find_duplicates(sys.argv[1], hashfun)
	except IndexError:
		print ("""Please pass a path to a directory with 
        duplicate files as a parameter to the script.""")
	if len(duplicateFIles) > 0:
		print ("Folder contains duplicate files")
		for file in duplicateFIles:
			print ("Filename is:		{0}".format(file))


