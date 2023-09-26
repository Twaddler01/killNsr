# KillNsr with GUI interface
# GUI with "kivy" modules
###################################################
# import modules
  
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.popup import Popup
import os
from os.path import join, isdir
import re
import glob
import shutil
from datetime import datetime

# window size
Window.size = (400, 500)

class MyLayout(AnchorLayout, BoxLayout):

	### class varisbles MyLayout.*
	search_input = ObjectProperty(None)
	replace_input = ObjectProperty(None)
	statuswintxt = ObjectProperty(None)
	custom_sr1 = ObjectProperty(None)
	custom_sr2 = ObjectProperty(None)
	data_path = os.getcwd()
	path_choice = False
	regex = False
	killn_done = False
		
	### WIP hide custom options until KillN is executedm
	def hide_widget(wid, dohide=True):
		if hasattr(wid, 'saved_attrs'):
			if not dohide:
				wid.opacity, wid.disabled = wid.saved_attrs
				del wid.saved_attrs
		elif dohide:
			wid.saved_attrs = wid.opacity, wid.disabled
			wid.opacity, wid.disabled = 0, True
			# other saved attr: wid.height = 0, wid.size_hint_y = Nome
	### hide custom_sr widgets
	#hide_widget(custom_sr)
	
	# get current date/time as dd/mm/YY H:M:S
	def getdatetime():
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
		return dt_string

	# FilePath popup functions
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Choose Folder", content=content, size_hint=(0.9, 0.9))
		self._popup.open()
			
	def load(self, path, selection):
		# get path to folder
		folder_path = os.path.abspath(path)
		
		# variables for folders
		MyLayout.data_path = folder_path
		MyLayout.output_path = folder_path + "/output/"
		MyLayout.load.output_path = MyLayout.output_path
		
		# abbreviate folder output dir string if too long to fit Label
		len_folder_path = len(folder_path)
		folder_path_trunc = folder_path[len_folder_path - 15:]
		if (len_folder_path > 15):
			self.ids.file_path_lbl.text = "Folder: [...] " + folder_path_trunc
		else:
			self.ids.file_path_lbl.text = "Folder: " + folder_path
		
		self.ids.statuswintxt.text = ""
		self.print_in_window("* Selected Data Folder: " + folder_path + "\n\n* Output folder to be created (if needed) or used: " + folder_path + "/output")
		MyLayout.path_choice = True
		self.dismiss_popup()

	# button: start initial killn process
	def btn(self):
		if (MyLayout.path_choice == False):
			self.ids.statuswintxt.text = "PLEASE SELECT A FOLDER"
		else:
			self.ids.statuswintxt.text = "STARTING KillNsr..."
			self.print_in_window("\n>> Log update: " + MyLayout.getdatetime() + "\n>> STARTING FOLDER SETUP...")

			# execute mod code
			MyLayout.start_killn(self)

	def on_checkbox_active(self, instance, value):
		MyLayout.regex = value

	# button of custom search/replace
	def process_sr(self):
		###WIP process_sr regex checkbox
		
		###WIP disable the inputs and button until KillN is done
		### custom_sr(file_path, searchstr, replacestr, isregex):
		self.print_in_window("\n>> Log update: " + MyLayout.getdatetime() + "\n>> STARTING CUSTOM SR...")
		# define variables
		searchstr = self.ids.search_input.text
		replacestr = self.ids.replace_input.text
		isregex = MyLayout.regex
		MyLayout.process_sr.count = 0
		MyLayout.process_sr.file_count = 0

		if (isregex == True):
			print("Regex is True ... WIP")
			### WIP
		# regular search/replace (outside if)
		else:
			print("Regex is False...proceeding with regular search and replace...")
			if (self.ids.search_input.text == ""):
				self.print_in_window('\n>> Please enter a search string...')
			else:
				# iterate files
				for file in MyLayout.start_killn.dir_list:
					if file.endswith(".txt"):
						with open(file, 'r') as f:
							# read file(s)
							infile = f.read()
							MyLayout.process_sr.count += infile.count(searchstr)
							MyLayout.process_sr.file_count += 1
							### TEMP disabled write
							#infile_searchstr = infile.replace(searchstr, replacestr)
							### write changes
							#f = open(output_file, "w")
							#f.write(infile_searchstr)
				self.print_in_window('\n>> Search string: "' + searchstr + '".\n>> Replacement string: "' + replacestr + '"')
				if (MyLayout.process_sr.count == 0):
					###TEST
					self.print_in_window('\n>> Search string: "' + searchstr + '" was not found in any files...')
					self.print_in_window("\n>> Waiting for additional custom search/replace requests...")		
				else:
					self.print_in_window("\n>> SUMMARY:\n- Files processed: " + str(MyLayout.process_sr.file_count) + "\n- Total custom replacement characters processed: " + str(MyLayout.process_sr.count))
					self.print_in_window("\n>> Waiting for additional custom search/replace requests...")		

	# button: reset everything
	def resetbtn(self):
		self.ids.search_input.text = ""
		self.ids.replace_input.text = ""
		self.ids.statuswintxt.text = ""
		self.ids.file_path_lbl.text = ""
		MyLayout.path_choice = False
		MyLayout.killn_done = False
		self.ids.custom_sr1.disabled, self.ids.custom_sr2.disabled = True, True
		self.ids.custom_sr1.opacity, self.ids.custom_sr2.opacity = 0, 0
	
	def print_in_window(self, thisvar):
		varattr = []
		self.thisvar = [varattr]
		for varattr in self.thisvar:
			self.ids.statuswintxt.text += thisvar
			last_attr = thisvar[-1]

	# dir_list -> sort files
	def sorted_alphanumeric(data):
		convert = lambda text: int(text) if text.isdigit() else text.lower()
		alpha_numkey = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
		return sorted(data, key = alpha_numkey)

	# CALL FUNCTION UPON SUBMIT BUTTON
	def start_killn(self):

		# main code
		MyLayout.start_killn.dir_list = MyLayout.sorted_alphanumeric(os.listdir(MyLayout.data_path))
		file_path = MyLayout.data_path + "/output/"
		os.chdir(MyLayout.data_path)
		
		try:
			os.mkdir("output")
			self.print_in_window('\n>> No output folder found, created new output subfolder "' + file_path + '"')
		except Exception as e:
			self.print_in_window('\n>> Searching for existing output subfolder...')
			if os.path.exists(file_path):
				self.print_in_window('\n>> Existing output subfolder...FOUND\n>> Using output subfolder "' + file_path + '"\n>> Using data folder: ' + MyLayout.data_path)
			else:
				self.print_in_window("\n>> ERROR: Unable to create output folder, please reset and try again...")				
				
		# check data folder files
		self.print_in_window('\n>> Searching for valid files in data folder...\n>> File(s) found:')
		for file in MyLayout.start_killn.dir_list:
			# Check whether file is in text format or not
			if file.endswith(".txt"):
				file_path = f"{file_path}{file}"
				self.print_in_window("\n" + file)
		MyLayout.process_files(self)

	# iterate killn removal of all files
	# saves a copy to /output and then modifies the files
	# .txt file limitation for now
	def process_files(self):
		# count files processed
		MyLayout.process_files.count = 0
		self.print_in_window('\n>> Copying files to ouput folder for processing...')
		for file in MyLayout.start_killn.dir_list:
			# Check whether file is in text format or not
			if file.endswith(".txt"):
				# make a copy to output folder for modification
				shutil.copy(file, MyLayout.output_path)
				# full pathto file
				file_path = f"{MyLayout.output_path}{file}"
				# start modification function(s)
				self.print_in_window('\n' + file_path)
				MyLayout.killn(file_path)
				MyLayout.process_files.count += 1
		self.print_in_window("\n>> Processed line removal (killN) on " + str(MyLayout.process_files.count) + " file(s) successfully (or no newline found)...DONE")
		self.print_in_window("\n>> SUMMARY:\n- Files processed: " + str(MyLayout.process_files.count) + "\n- Total newline characters removed: " + str(MyLayout.killn.count))
		self.print_in_window("\n>> Waiting for custom search/replace requests...")		
		# KillN was completed, show hidden widgets now
		MyLayout.killn_done = True
		self.ids.custom_sr1.disabled, self.ids.custom_sr2.disabled = False, False
		self.ids.custom_sr1.opacity, self.ids.custom_sr2.opacity = 1, 1
	#WIP
	# READY FOR CUSTOM SEARCH/REPLACE
	def custom_sr(file_path, searchstr, replacestr, isregex):
		MyLayout.custom_sr.count = 0
		
		for output_file in glob.glob(file_path):
			with open(output_file, 'r') as f:
				infile = f.read()
				MyLayout.custom_sr.count += infile.count(searchstr)
				# TEST
				
				#infile_custom_sr = infile.replace(search_str, replace_str)
				# write changes
				#f = open(output_file, "w")
				#f.write(infile_custom_sr)

	# read files, process changes, and save the changes
	def killn(file_path):
		MyLayout.killn.count = 0
		# iterate files
		for output_file in glob.glob(file_path):
			with open(output_file, 'r') as f:
				# read file(s)
				infile = f.read()
				MyLayout.killn.count += infile.count('\n')
				infile_killn = infile.replace('\n', '')
				# write changes
				f = open(output_file, "w")
				f.write(infile_killn)

class LoadDialog(BoxLayout):
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)
	
	# dir only
	def is_dir(self, directory, filename):
		return isdir(join(directory, filename))

class MyApp(App):
    pass
    
    #def build(self):
        #return MyLayout()

Factory.register('MyLayout', cls=MyLayout)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == "__main__":
    MyApp().run()
