#Проприетарное ПО
#Версия 1.0.1

from tkinter import *
import threading
import math

root = Tk()
root.geometry('1060x560')

# Начальные параметры 
length = [0.50,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58]
phi_0 = []
oval = []
t = 0.0
x = 50

canv = Canvas(root, width=1050, height=550)
canv.place(x=5, y=5)

for i in range(9):
	phi_0.insert(i,math.atan(0.15/length[i]))
	oval.insert(i, canv.create_oval(x,50-25,x+50,50+25,fill="black"))
	x+=100



def f():
	global canv
	global oval
	global t
	global phi_0
	global length
	i = 0

	for i in range(9):
#		y = math.ceil(length[i]*math.sin(phi_0[i])*math.sin(math.sqrt(9.8/length[i])*t+phi_0[i])*50)
		canv.move(oval[i], 0, math.ceil(length[i]*math.sin(phi_0[i])*math.sin(math.sqrt(9.8/length[i])*t+phi_0[i])*50-0.5))

	if t==10000:
		t=0
	t+=0.01
	root.after(10, f)	

	return 0

f()

root.mainloop()
