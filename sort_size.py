#!/usr/bin/python2

import commands
import os

def home():
	z=os.path.expanduser('~')
	return z

def desktop():
	z=os.path.join(os.path.expanduser('~'), 'Desktop')
	return z

def downloads():
	z=os.path.join(os.path.expanduser('~'), 'Downloads')
	return z

def documents():
	z=os.path.join(os.path.expanduser('~'), 'Documents')
	return z

def pictures():
	z=os.path.join(os.path.expanduser('~'), 'Pictures')
	return z

def sort(b):
	a=commands.getstatusoutput("sudo du -ah {0} | sort -rh | head -10".format(b));
	if a[0]==0:
		print a[1]
	else:
		pass

print("Select Folder")
print("1.Home")
print("2.Desktop")
print("3.Downloads")
print("4.Documents")
print("5.Pictures")

choice = int(input("Enter choice(1/2/3/4/5):"))

if choice == 1:
	b=home()
	sort(b)

elif choice == 2:
	b=desktop()
	sort(b)
	
elif choice == 3:
	b=downloads()
	sort(b)

elif choice == 4:
	b=documents()
	sort(b)

elif choice == 5:
	b=pictures()
	sort(b)	

else:
	print "Wrong Input"

