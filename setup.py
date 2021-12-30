from tkinter import *
import json
from tkinter.colorchooser import askcolor
from random import randint

def format_color(color):
	return (int(color[1] + color[2], 16), int(color[3] + color[4], 16), int(color[5] + color[6], 16))
	
def random_color() -> tuple:
	red = randint(0, 255)
	green = randint(0, 255)
	blue = randint(0, 255)
	return (red, green, blue)

class ParticleSetup:
	def __init__(self, win):
		# Creating Labels for entries
		self.lbl_x_pos = Label(win, text='X position:')
		self.lbl_y_pos = Label(win, text='Y position:')
		self.lbl_x_vel = Label(win, text='X velocity:')
		self.lbl_y_vel = Label(win, text='Y velocity:')
		self.lbl_mass = Label(win, text='Mass')
		
		# Creating Entries
		self.t_x_pos = Entry()
		self.t_y_pos = Entry()
		self.t_x_vel = Entry()
		self.t_y_vel = Entry()
		self.t_mass = Entry()
		
		# Creating Select a Color Button
		self.btn_color = Button(win, text="Select a Color", command=self.change_color)
		
		# The make and clear button
		self.btn_clr = Button(win, text='Clear', command=self.clear)
		self.btn_make = Button(win, text='Make', command=self.make)
		self.btn_clr_all = Button(win, text='Clear All', command=self.wipe)
		
		# Positioning Labels and Entries
		self.lbl_x_pos.grid(row = 0, column = 0)
		self.t_x_pos.grid(row = 0, column = 1)
		
		self.lbl_y_pos.grid(row = 1, column = 0)
		self.t_y_pos.grid(row = 1, column = 1)
		
		self.lbl_x_vel.grid(row = 2, column = 0)
		self.t_x_vel.grid(row = 2, column = 1)
		
		self.lbl_y_vel.grid(row = 3, column = 0)
		self.t_y_vel.grid(row = 3, column = 1)
		
		self.lbl_mass.grid(row = 4, column = 0)
		self.t_mass.grid(row = 4, column = 1)
		
		self.btn_color.grid(row = 5, column = 0)
		
		# Positioning buttons
		self.btn_clr.grid(row = 6, column = 0, padx = 10, pady = 10)
		self.btn_make.grid(row = 6, column = 1, padx = 10, pady = 10)
		self.btn_clr_all.grid(row = 7, column = 0, padx = 10, pady = 10)
		
	def change_color(self):
		self.colors = askcolor(title="Choose a Color")	
	
	def clear(self):
		# Clearing everything here
		self.t_mass.delete(0, 'end')
		self.t_x_pos.delete(0, 'end')
		self.t_y_pos.delete(0, 'end')
		self.t_x_vel.delete(0, 'end')
		self.t_y_vel.delete(0, 'end')
		
	def make(self):
		# Getting the attributes
		try:
			new_mass = int(self.t_mass.get())
		except ValueError:
			new_mass = 0
			
		try:
			new_x_pos = int(self.t_x_pos.get())
		except ValueError:
			new_x_pos = 0
		
		try:
			new_y_pos = int(self.t_y_pos.get())
		except ValueError:
			new_y_pos = 0
	
		try:
			new_x_vel = int(self.t_x_vel.get())
		except ValueError:	
			new_x_vel = 0
		
		try:
			new_y_vel = int(self.t_y_vel.get())
		except ValueError:
			new_y_vel = 0
			
		try:
			new_color = format_color(self.colors[1])
		except IndexError:
			new_color = random_color()
		
		json_data = {"x" : new_x_pos, "y" : new_y_pos,"x_velos" : new_x_vel,"y_velos" : new_y_vel,"mass" : new_mass, "color" : new_color}
		
		# Load Json data
		with open("particles.json", "r") as file:
			data = json.load(file)	
		
		data["particles"].append(json_data)
		
		# Add Json data
		with open("particles.json", "w") as file:
			json.dump(data, file, indent = 4)
			
		self.clear()
			
	def wipe(self):
		# Wipes all json data
		with open("particles.json", "w") as file:
			json.dump({"particles" : [] }, file, indent = 4)
		
		self.clear()
		
window = Tk()
ParticleSetupWindow = ParticleSetup(window)
window.title('Particle Collision Simulator Setup')
window.mainloop()