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
from kivy.properties import StringProperty
# window size
Window.size = (400, 500)

class MyLayout(AnchorLayout, BoxLayout):
	"""    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("Name:", self.name.text, "email:", self.email.text)
        self.name.text = ""
        self.email.text = ""
	"""
	name = ObjectProperty(None)
	stored_txt = ObjectProperty(None)

	def btn(self):
		self.name.text = "Name: " + self.name.text + "\n"
		print(self.name.text)
		self.name.text = ""

	def resetbtn(self):
		self.name.text = ""

#class AddOutput(TextInput):

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()
