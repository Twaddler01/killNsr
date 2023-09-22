# Import Modules
import os
import glob
import shutil
import re
  
# Folder Paths
# folders: "PARSE DATA" = main.py (script folder)
# subfolders:"/data" subfolder = input files, "/output" subfolder = output files

# define file paths
script_path = os.getcwd()
print("Main folder =", script_path)
output_path = script_path + "/output/"
data_path = script_path + "/data/"

# create subfolders if needed
try:
	os.mkdir("output")
	print("Created new output subfolder 'output'...")
except OSError as error:
		print("Output subfolder...OK")
try:
	os.mkdir("data")
	print("Created DATA subfolder, pleaae place input files here, then run again. EXITING...")
	exit()
except OSError as error:
	print("Data subfolder..OK")

# Change the directory
os.chdir(data_path)
  
# Read text file

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        regtxt = f.read()
        print("Original txt:\n", regtxt)
        f.close()

def print_text_nolines(file_path):
    with open(file_path, 'r') as f:
        intxt = f.read()
        newtxt = intxt.replace('\n', '')
        print("New txt:\n", newtxt)
        f.close()
        return newtxt

def sorted_alphanumeric(data):
	convert = lambda text: int(text) if text.isdigit() else text.lower()
	alpha_numkey = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
	return sorted(data, key = alpha_numkey)

# sort list using function if needed (WIP)
dir_list = sorted_alphanumeric(os.listdir(data_path))

def killn(file_path):
	for output_file in glob.glob(file_path):

		with open(output_file, 'r') as f:
						
			# write to file(s)
			infile = f.read()
			
			# REMOVE ALL NEW LINES
			infile_killn = infile.replace('\n', '')
			f = open(output_file, "w")
			f.write(infile_killn)

def search_replace_inFiles(output_path, sr_args1, sr_args2):
# count files processed
	search_replace_inFiles.sr_count = 0
	for file in dir_list:
		# Check whether file is in text format or not
		if file.endswith(".txt"):
			# make a copy to output folder for modification
			# -- DONE IN killn -- shutil.copy(file, output_path)
			# full path to file
			file_path = f"{output_path}/{file}"
			
		#for output_file in glob.glob(file_path):
			with open(file_path, 'r') as f:
				# write to file(s)
				infile = f.read()
				# process user replacements
				try:
					infile_repl = infile.replace(sr_args1, sr_args2)
					f = open(file_path, "w")
					f.write(infile_repl)
					search_replace_inFiles.sr_count += 1
					print("File", file, "processed user replacements sucessfully...")
				except OSError as error:
					print("Search/replace resulted in error...please try again.")	
					break
					
	#for output_file in glob.glob(file_path):
	#try:
		#sr_args1 = input("Search ALL of String(s): ")
		#sr_args2 = input("Replace ALL of String(s): ")
		#infile_next = infile.replace(sr_args1, sr_args2)
		#f.write(infile_next)
	#entry_string = input("Enter another replacement string? (y/n): ")
	#except OSError as error:
		#print("Search/replace resulted in error...please try again.")
		#entry_string = input("Enter another replacement string? (y/n): ")

# iterate killn removal of all files
def process_files():
	# count files processed
	process_files.count = 0
	for file in dir_list:
		# Check whether file is in text format or not
		if file.endswith(".txt"):
			# make a copy to output folder for modification
			shutil.copy(file, output_path)
			# full path to file
			file_path = f"{output_path}/{file}"
			# call text file functions
			#read_text_file(output_path)
			#print_text_nolines(file_path)
			killn(file_path)
			process_files.count += 1
			print("File", file, "processed line removal (killn) sucessfully...")

process_files()
print("Removed new lines...DONE")
entry_string = input("Enter new replacement string? (y/n): ")
while entry_string == 'y':
	# USER REPLACEMENTS -- WIP
	sr_args1 = input("Search ALL of String(s): ")
	sr_args2 = input("Replace ALL of String(s): ")
	search_replace_inFiles(output_path, sr_args1, sr_args2)
	print("\nTotal files of user replacements:", search_replace_inFiles.sr_count)
	entry_string = input("Enter new replacement string? (y/n): ")
	if entry_string != 'y':
		print("Thank you for using Killn! :)")
		break
