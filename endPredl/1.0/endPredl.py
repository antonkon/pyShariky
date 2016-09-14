from tkinter import *

root = Tk()

root.geometry('800x400')

text1 = Text(root,width=55,height=26,wrap=WORD)
text1.pack(side = 'left')
text2 = Text(root, width=55,height=26,wrap=WORD)
text2.pack(side = 'right')

f = open('1','r')
text1.insert(INSERT,f.read())
f.close()

f = open('2','r')
text2.insert(INSERT,f.read())
f.close()

root.mainloop()
