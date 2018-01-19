import tkinter as tk

window = tk.Tk()
window.title("radio button")


l = tk.Label(window, bg='red', width=20, text='empty')
l.pack()


def print_selection(val):
    """传入的是当前滑轮的位置值, 是str类型"""
    # print(type(val))
    l.config(text=val)

s = tk.Scale(window, label='拉动我', from_=5, to=11,
             orient=tk.HORIZONTAL, length=200,
             showvalue=0, tickinterval=3,
             resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
