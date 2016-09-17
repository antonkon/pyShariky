#Проприетарное ПО
#Версия 2.0.1

#fjslakjfldasjklfjkasljkfl;asdjl;fjkdl;asjkfkl;d

from tkinter import *
import threading
import math

root = Tk()
root.geometry('560x1060')

#Тут у нас немного данных:
#Физические константы:
g = 2090.81

#Начальные параметры системы, определяемые нами:
x_ampl = 80 		#Не может быть больше длины самой короткой нити (палочка) 

quant_ball = 6
radius_ball = 25
dist_center_ball_y = 100

lenght_min = 100 #Минимальная длина нити

#Начальные параметры системы, зависящие от определяемых нами параметров:
lenght = [] #Длины нитей на которых подвешены шарики
for i in range(quant_ball):
	lenght.insert(i, lenght_min + dist_center_ball_y*i)

omega = []
phi_0 = []
y_min = []  	#
y_ampl = []		#

#Размеры холста:
canv_height = lenght_min + (quant_ball-1)*dist_center_ball_y + radius_ball
canv_width = canv_height * 0.7

#Переменные системы:
x = []		# x(t)
y = []		# y(t)
x_real = []
y_real = []

#Прочее:
oval = []
t = 0

canv = Canvas(root, width=canv_width, height=canv_height)
canv.place(x=5, y=5)

#Тут у нас всякие прикольные функции:
#--------------------------------------------------------------------------------
#Функция, определяющая начальные параметры системы:
def creat(col=6):
	global canv
	global oval
	
	global t
	global omega
	global phi_0
	global y_min
	global y_ampl
	i = 0
	

	
	
	for i in range(col):

		#Начальные параметры системы, зависящие от определяемых нами параметров:
		omega.insert(i, math.sqrt(g/lenght[i]))
		phi_0.insert(i, math.asin(x_ampl/lenght[i]))
		y_min.insert(i, lenght[i] * math.cos(phi_0[i]))
		y_ampl.insert(i, (lenght[i]-y_min[i])/2)

		i+=1

	i=0
	canv.delete('all')
	for i in range(col):

		#Значения относительно центра холста:
		x.insert(i, x_ampl * math.sin(omega[i]*t + phi_0[i]))
		#y[i] = y_min[i] + y_ampl[i]			#Пока что так пусть будет

		#Реальные значения:
		x_real.insert(i, canv_width/2 + x[i])
		#y_real.insert(i, canv_height/2) + y[i])
		
		oval.insert(i, canv.create_oval([x_real[i]-radius_ball,y_min[i]-radius_ball], [x_real[i]+radius_ball,y_min[i]+radius_ball], fill="black"))
		
		i+=1
	if t == 10000: 
		t=0
	t+=0.01
	root.after(1, creat)	

	return 0

#--------------------------------------------------------------------------------
def motion(col=9):
	i = 0
	global canv
	#global canv1
	#global x
	#global y
	#global x_real
	global x_real

	global t
	x = 50

	
	return 0

#Самая главная функция или что-то типо того
creat(6)

#root.after_idle(motion)
root.mainloop()
