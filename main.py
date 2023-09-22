# Killn with GUI interface
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
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.popup import Popup
import os
from os.path import join, isdir
from datetime import datetime

# window size
Window.size = (400, 500)

class MyLayout(AnchorLayout, BoxLayout):

	name_input = ObjectProperty(None)
	entry2 = ObjectProperty(None)
	statuswintxt = ObjectProperty(None)
	data_path = os.getcwd()
	
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
		#self.path = folder_path
		
		# variables for processing
		# set default dir from CWD to path selected
		MyLayout.data_path = folder_path
		print("Global data path changed to:", MyLayout.data_path)
		print("data_path =", folder_path)
		output_path = folder_path + "/output/"
		print("output_path =", output_path)
		
		# abbreviate folder output dir string if too long to fit Label
		len_folder_path = len(folder_path)
		folder_path_trunc = folder_path[len_folder_path - 15:]
		if (len_folder_path > 15):
			self.ids.file_path_lbl.text = "Folder: [...] " + folder_path_trunc
		else:
			self.ids.file_path_lbl.text = "Folder: " + folder_path

		self.print_in_window("\n>> Log update: " + MyLayout.getdatetime() + "\n>> FOLDER SETUP...")
		folder_path = "\n>> Using Folder: " + folder_path + "\n>> Output folder will be: " + folder_path + "/output"
		self.print_in_window(folder_path)
		self.dismiss_popup()
		
		#return self.path


	#submit button TEST
	def btn(self):
		self.print_in_window("\n>> Log update: " + MyLayout.getdatetime() + "\n>> FOLDER SETUP...")
		
		#print("Global path (default):", MyLayout.data_path)
		self.print_in_window("\n>> Path (default CWD): " + MyLayout.data_path)
		self.print_in_window("\n>> SELECT FOLDER ABOVE TO CHANGE -- NOTE: An output subfolder (/output/) will be used or created for output files... Currently it will be in " + MyLayout.data_path + "/output/")
		#self.print_in_window("\n>> UPDATING INPUTS...")
		#self.print_in_window("\n>> " + self.ids.name_input.text)
		#self.print_in_window("\n>> " + self.ids.entry2.text)

	# clear all fields
	def resetbtn(self):
		self.ids.entry2.text = ""
		self.ids.name_input.text = ""
		self.ids.statuswintxt.text = ""
	
	def print_in_window(self, thisvar):
		varattr = []
		self.thisvar = [varattr]
		for varattr in self.thisvar:
			self.ids.statuswintxt.text += thisvar

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
