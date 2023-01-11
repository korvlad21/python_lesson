from tkinter import *

root = Tk()
root.geometry('400x200')
root.title('Игра в кости. Сделай бросок!')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file=('iconka.png')))
font = PhotoImage(file=('holst.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()