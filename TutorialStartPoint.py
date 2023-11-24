import threading
import time
import os
import sys
import subprocess

def RunBatchFile():
	args = ['VS_Build.bat']
	result = subprocess.run(args)

def RunGitCommand():	
	# # Checking git status
	statusResult = subprocess.run(['git', 'status'], capture_output=True, check=True)
	print(statusResult.stdout.decode("ascii"))
	file = open("gitstatusresult.txt", "w")
	file.write("--Status--\n")
	file.write(statusResult.stdout.decode("ascii"))
	file.close()

	# # getting head commit git repo
	getHeadCommitResult = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, check=True)
	print(getHeadCommitResult.stdout.decode("ascii"))
	file = open("headcommitresult.txt", "w")
	file.write("--Commit being ran--\n")
	file.write(getHeadCommitResult.stdout.decode("ascii"))
	file.close()

	# # pulling git repo
	pullResult = subprocess.run(["git", "pull"], capture_output=True, check=True)
	print(pullResult.stdout.decode("ascii"))
	file = open("pullresult.txt", "w")
	file.write("--Pull result--\n")
	file.write(pullResult.stdout.decode("ascii"))
	file.close()

def PollForChanges():
	print(time.ctime())
	RunBatchFile()
	RunGitCommand()

def RunForever():
	WAIT_TIME_SECONDS = 5
	ticker = threading.Event()
	while not ticker.wait(WAIT_TIME_SECONDS):
		PollForChanges()

PollForChanges()
##RunForever()