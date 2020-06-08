from tkinter import *
from tkinter import messagebox

root = Tk()

new_window = Toplevel()
new_window.withdraw()
# frame_labels = tkinter.Frame(root, borderwidth="2", relief="ridge")
# frame_buttons = tkinter.Frame(root, borderwidth="2", relief="ridge")
# frame_labels.grid(column=0, row=0, sticky="ns")
# frame_buttons.grid(column=1, row=0)

root.title("Hello!")

root.resizable(width="false", height="false")

root.minsize(width=300, height=350)
root.maxsize(width=300, height=350)

simple_label = Label(root, text="Easy, right?")
closing_button = Button(root, text="Close window", command=root.destroy)

simple_label.pack()
closing_button.pack()

C = Canvas(root, bg = "blue", height = 250, width = 300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 250, fill = "red")
line = C.create_line(10,10,200,200,fill = 'white')
C.pack()

root.mainloop()  