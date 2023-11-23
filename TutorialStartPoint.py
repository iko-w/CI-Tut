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

	# # pulling git repo
	pullResult = subprocess.run(["git", "pull"], capture_output=True, check=True)
	print(pullResult.stdout.decode("ascii"))


def PollForChanges():
	print(time.ctime())
	RunBatchFile()
	RunGitCommand()

def RunForever():
	WAIT_TIME_SECONDS = 5
	ticker = threading.Event()
	while not ticker.wait(WAIT_TIME_SECONDS):
		PollForChanges()

# #PollForChanges()
RunForever()