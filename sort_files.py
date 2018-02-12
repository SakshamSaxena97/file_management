#usr/bin/python2

import os
import commands
import shutil

move_files=[]
move_from=os.path.expanduser('~/Desktop/')
z=os.path.join(os.path.expanduser('~'), 'Documents')

move_files += [ [ "png" , os.path.join(os.path.expanduser('~'), 'Documents/pics/') ] ]
move_files += [ [ "jpg" , os.path.join(os.path.expanduser('~'), 'Documents/pics/') ] ]
move_files += [ [ "mp3" , os.path.join(os.path.expanduser('~'), 'Documents/music/') ] ]
move_files += [ [ "mkv" , os.path.join(os.path.expanduser('~'), 'Documents/videos/') ] ]
move_files += [ [ "mp4" , os.path.join(os.path.expanduser('~'), 'Documents/videos/') ] ]
move_files += [ [ "pdf" , os.path.join(os.path.expanduser('~'), 'Documents/PDF/') ] ]
move_files += [ [ "docx" , os.path.join(os.path.expanduser('~'), 'Documents/DOC/') ] ]
move_files += [ [ "avi" , os.path.join(os.path.expanduser('~'), 'Documents/videos/') ] ]
move_files += [ [ "doc" , os.path.join(os.path.expanduser('~'), 'Documents/DOC/') ] ]
move_files += [ [ "py" , os.path.join(os.path.expanduser('~'), 'Documents/codes/') ] ]
move_files += [ [ "pl" , os.path.join(os.path.expanduser('~'), 'Documents/codes/') ] ]
move_files += [ [ "c" , os.path.join(os.path.expanduser('~'), 'Documents/codes/') ] ]
move_files += [ [ "cpp" , os.path.join(os.path.expanduser('~'), 'Documents/codes/') ] ]
move_files += [ [ "scala" , os.path.join(os.path.expanduser('~'), 'Documents/codes/') ] ]
move_files += [ [ "java" , os.path.join(os.path.expanduser('~'), 'Documents/codes/') ] ]
move_files += [ [ "class" , os.path.join(os.path.expanduser('~'), 'Documents/codes/') ] ]


case_sensitive = False




testing = True



#-------------do not change anything else---------------------------------------

move_ext = []
move_loc = []

cancel = False

for i in range(len(move_files)):

    input_ext = move_files[i][0]
    input_loc = move_files[i][0]

    if not case_sensitive:
        move_ext += [move_files[i][0].lower()]
        input_ext = input_ext.lower()
    else:
        move_ext += [move_files[i][0]]

    move_loc += [move_files[i][1]]

    if move_ext.count(input_ext) > 1:
        cancel = True
        print "\nError: Duplicate entry for extension \"%s\". Please modify the move criteria." % input_ext
        print "       Cancelling the move operation\n"
        break


if not cancel:

    if testing:


    	print "\nWill move the following:"
    for m in range(len(move_ext)):
        print "    All  .%-6s files will move to:   %s" % (move_ext[m], move_loc[m])
    if case_sensitive:
        print "\nAll extensions are case-sensitive"
    print

    print "\nFiles to move:"
    move_names = []
    skip_files = ["desktop.ini", "Thumbs.db"]
    for cur_file_name in os.listdir(move_from):
        cur_path = os.path.join(move_from, cur_file_name)

        #skip directories
        if os.path.isdir(cur_path):
            continue

        #skip system files
        if cur_file_name in skip_files:
            continue

        #skip temporary files
        if cur_file_name[0:1] == "~":
            continue


        #file_name = file_full_name.split(".")[0]
        #print "\n" + cur_file_name

        cur_ext = cur_file_name.split(".")[-1]
        if cur_ext in move_ext:
            #print "MOVE"
            move_index = move_ext.index(cur_ext)

            move_names += [[cur_file_name, move_index]]
            print "    %s" % cur_file_name

    if len(move_names) == 0:
        print "    No files found with the defined extensions"

    moved_file_count = 0
    for cur_move in move_names:
	cur_path=move_from+cur_move[0]
	#print cur_path
	new_path=move_loc[cur_move[1]]+cur_move[0]
	#print new_path
	#print cur_move[0]
	#print move_names[cur_move[1]][0]
	if cur_move[0].endswith('.png') or cur_move[0].endswith('.jpg'):
		if not os.path.exists(move_loc[cur_move[1]]):
			os.makedirs(move_loc[cur_move[1]])
			print "new folder pics created"
			shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
			print "moved"
		else:
			#shutil.rmtree(move_loc[cur_move[1]])
    			#os.makedirs(move_loc[cur_move[1]])
			print "folder pics already present"
			shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
			print "moved"

	if cur_move[0].endswith('.mp3'):
		if not os.path.exists(move_loc[cur_move[1]]):
			os.makedirs(move_loc[cur_move[1]])
			print "new folder music created"
			shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
			print "moved"
		else:
			#shutil.rmtree(move_loc[cur_move[1]])
    			#os.makedirs(move_loc[cur_move[1]])
			print "folder music already present"
			shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
			print "moved"

	if cur_move[0].endswith('.mkv') or cur_move[0].endswith('.mp4') or cur_move[0].endswith('.avi'):
		if not os.path.exists(move_loc[cur_move[1]]):
			os.makedirs(move_loc[cur_move[1]])
			print "new folder videos created"
			shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
			print "moved"
		else:
			#shutil.rmtree(move_loc[cur_move[1]])
    			#os.makedirs(move_loc[cur_move[1]])
			print "folder videos already present"
			shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
			print "moved"


	if cur_move[0].endswith('.pdf'):
		if not os.path.exists(move_loc[cur_move[1]]):
			os.makedirs(move_loc[cur_move[1]])
			print "new folder pdf created"
			shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
			print "moved"
		else:
			#shutil.rmtree(move_loc[cur_move[1]])
    			#os.makedirs(move_loc[cur_move[1]])
			print "folder pdf already present"
			shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
			print "moved"

	if cur_move[0].endswith('.docx') or cur_move[0].endswith('.doc'):
		if not os.path.exists(move_loc[cur_move[1]]):
			os.makedirs(move_loc[cur_move[1]])
			print "new folder DOC created"
			shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
			print "moved"
		else:
			#shutil.rmtree(move_loc[cur_move[1]])
    			#os.makedirs(move_loc[cur_move[1]])
			print "folder DOC already present"
			shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
			print "moved"

	if cur_move[0].endswith('.py') or cur_move[0].endswith('.c') or cur_move[0].endswith('.cpp') or cur_move[0].endswith('.pl') or cur_move[0].endswith('.scala') or cur_move[0].endswith('.java') or cur_move[0].endswith('.class'):
			if not os.path.exists(move_loc[cur_move[1]]):
				os.makedirs(move_loc[cur_move[1]])
				print "new folder codes created"
				shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
				print "moved"
			else:
				#shutil.rmtree(move_loc[cur_move[1]])
	    			#os.makedirs(move_loc[cur_move[1]])
				print "folder codes already present"
				shutil.move(os.path.join(move_from,cur_move[0]), os.path.join(move_loc[cur_move[1]],cur_move[0]))
				print "moved"
