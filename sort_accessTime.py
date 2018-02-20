#/usr/bin/python

import os
import time
import commands
from subprocess import call
import sys
import glob
import datetime

def desktop():
	z=os.path.join(os.path.expanduser('~'), 'Desktop')
	return z

def downloads():
	z=os.path.join(os.path.expanduser('~'), 'Downloads')
	return z

def clean(b):
	removed=0
	current_time=time.time()
	path = b

	dir_to_search = os.getcwd()
	print "Current working directory %s" % dir_to_search

	if dir_to_search != "full desired path":
	# Now change the directory
		os.chdir( path ) 
	      # Check current working directory.
		dir_to_search = os.getcwd()
		print "Directory changed successfully %s" % dir_to_search

	for dirpath, dirnames, filenames in os.walk(dir_to_search):
		for file in filenames:
			curpath = os.path.join(dirpath, file)
	       	        #print curpath
			file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(curpath))
			#print file_modified
			#q=datetime.datetime.now() - file_modified > datetime.timedelta(weeks=15)
			#print curpath	
			if datetime.datetime.now() - file_modified > datetime.timedelta(weeks=15):
				print "This file is not modified from past 15 weeks: ",curpath
			
				while True:
					    try:
	
						x=raw_input("Can I remove it (y/n): ")
						if x == "y":
							os.remove(curpath)
							removed=removed+1
							print "removed"
						elif x== "n":
							print "Chill.... nothing removed"
					
						else:
							continue

					    except ValueError:
					
							print("Sorry, I didn't understand that.")
							continue

					    else:
	
						break			
			
			
	print "Currently present files are either modified from the past 15 weeks or refused by the user to delete "			
				

print("Select Folder")
print("1.Desktop")
print("2.Downloads")

choice = int(input("Enter choice(1/2/3/4/5):"))

if choice == 1:
	b=desktop()
	clean(b)

elif choice == 2:
	b=downloads()
	clean(b)

else:
	print "Wrong Input"

	
