from tkinter import *
root = Tk()

frame = Frame(root)
frame.pack()

buttonFrame= Frame(root)
buttonFrame.pack(side=BOTTOM)
redbutton= Button(frame,text='u', fg= 'red')
redbutton.pack(side=LEFT)
greenbutton = Button(frame, text= 'T', fg='green')
greenbutton.pack(side=LEFT)
brownbutton= Button(frame, text= 's', fg='brown')
brownbutton.pack(side=LEFT)
cyanbutton= Button(frame, text='R', fg='cyan')
cyanbutton.pack(side=LEFT)
bluebutton = Button(frame, text='Q', fg='blue')
bluebutton.pack(side=LEFT)
orangebutton = Button(frame, text= 'p', fg='orange')
orangebutton.pack(side= LEFT)
mainloop()