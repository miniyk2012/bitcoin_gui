import tkinter as tk


window = tk.Tk()
window.title("radio button")

var = tk.StringVar()

l = tk.Label(window, bg='red', width=20, text='empty')
l.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()


def print_selection():
    if var1.get() == 1 and var2.get() == 1:
        l.config(text="I love both")
    elif var1.get() == 1 and var2.get() == 0:
        l.config(text="I love python")
    elif var1.get() == 0 and var2.get() == 1:
        l.config(text="I love c++")
    else:
        l.config(text="I hate both")


c1 = tk.Checkbutton(window, variable=var1, onvalue=1, offvalue=0,
                    command=print_selection, text='python')
c2 = tk.Checkbutton(window, variable=var2, onvalue=1, offvalue=0,
                    command=print_selection, text='C++')  # 选中var2变成onvalue, 否则是offvalue
c1.pack()
c2.pack()
window.mainloop()


