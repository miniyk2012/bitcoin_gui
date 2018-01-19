import tkinter as tk


window = tk.Tk()
window.title("radio button")

var = tk.StringVar()

l = tk.Label(window, bg='red', width=20, text='empty')
l.pack()


def print_selection():
    l.config(text="You have selected " + var.get())

r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)  # 当你选中它时，var会被设置为value的值，然后再执行command
r1.pack()

r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text='Option B', variable=var, value='C', command=print_selection)
r3.pack()

window.mainloop()