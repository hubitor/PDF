files = {}
 
for filename in os.listdir():
    if os.path.isfile(filename) \
       and f.endswith(".txt") \
       and not filename in files:
        with open(filename, "r") as file:
            files[filename] = file.read()
 
for filename, text in files.items():
    print(filename)
    print("=" * 80)
    print(text)


from itertools import zip_longest
 
# Open two files at the same time using with
with open('file1.txt') as file1, open('file2.txt') as file2:
	# Since every open file is an iterator you can pass them to
	# zip to get the files read simultaneously in one loop.
	for line1, line2 in zip_longest(file1, file2):
		process(line1, line2)


from itertools import zip_longest
import glob
 
# Find all *.txt files in the directory
file_name_list = glob.glob('*.txt')
 
# Try to open all of the files
# Can't use 'with' as we have an unknown set of files
 
# Open all of the files - trapping exceptions as we go
try:
	open_files = [open(file_name) for file_name in file_name_list]
except OSERROR:
	raise 
 
# Read all the lines at the same time
# unpack the open_files list into zip
# each open file is an iterator in it's own right
try:
	for lines in zip_longest(*open_files):
		# lines will be a tuple of all of the
		# corresponding lines from the files
		process_multiple_lines(lines):
except:
	raise
finally:
	#since we aren't using a context manager (with)
	# we have to ensure all files get closed.
	for open_file in open_files:
		open_file.close()

import os
file_content =[]
dir = "YOUR_FOLDER_PATH"
for file in os.path.listdir( dir ):
  if file.endswith( ".txt" ):
    try:
      with open( os.path.join( dir, file ) ,"r") as fd:
        file_content.append( fd.read )
    Exception,e:
       print e
