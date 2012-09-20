#!/usr/bin/env python
"""
test.py

Created by Dale Karp on 2012-09-19.
"""
import os
import sys
import subprocess
import commands

def main():
	# variables needed
	good_test_dir = os.path.realpath("good")
	bad_test_dir = os.path.realpath("bad")
	fail_count = 0
	fail_list = []

	# first, check for webvtt-parser npm package
	status, results = commands.getstatusoutput("webvtt")

	if status == 32512: # 32512 is 'command not found' in python's OS module exit codes
		print "webvtt is not installed. Please make sure you have Node.js and NPM installed and then type:"
		print "npm install webvtt"
		print "on the command line."
		sys.exit()

	# get a list of files for good and bad tests
	good_files = os.listdir(good_test_dir)
	bad_files = os.listdir(bad_test_dir)

	# run good tests
	for good_file in good_files:
		# get file's absolute path
		file_path = os.path.join(good_test_dir, good_file)
		# run file against webvtt parser
		retcode = subprocess.call(["webvtt", file_path], stdout=subprocess.PIPE)
		# if we did NOT get 0 (pass), add file to fail list & increase fail count.
		if retcode != 0:
			fail_count = fail_count + 1
			fail_list.append(file_path)

	# run bad tests
	for bad_file in bad_files:
		file_path = os.path.join(bad_test_dir, bad_file)
		retcode = subprocess.call(["webvtt", file_path], stdout=subprocess.PIPE)
		# if we did NOT get 1 (fail), add file to fail list & increase fail count.
		if retcode != 1:
			fail_count = fail_count + 1
			fail_list.append(file_path)

	# sum up them fails!
	if fail_count > 0:
		print "It seems that", fail_count, "file" if fail_count == 1 else "files", "have failed to pass, or passed when they should have failed!"
		print "Here is a list of said files:"
		for fname in fail_list:
			print fname

if __name__ == '__main__':
 status = main()
 sys.exit(status)