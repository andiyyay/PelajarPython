from tkinter import*

master = Tk()
w = Canvas(master, width=60, height=80)
w.pack()
canvas_height = 40
canvas_widht = 200
y = int(canvas_height/2)
w.create_line(0,y,canvas_widht,y)
mainloop()