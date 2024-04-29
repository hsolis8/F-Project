import tkinter as tkroot = tk.Tk()

root.title("User Account")

master = Tk()
Label(master, text='Id').grid(row=0)
Label(master, text='Pin').grid(row=1)
Label(master, text= 'Name').grid(row=2)
Label(master, text= 'Balance').grid(row=3)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
mainloop()

