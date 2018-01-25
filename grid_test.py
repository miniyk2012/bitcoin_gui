import tkinter as tk


window = tk.Tk()
window.geometry("500x500")
window.title("grid_test")

fm1 = tk.Frame(window)
fm1.grid(row=1, column=1)
fm2 = tk.Frame(window)
fm2.grid(row=1, column=2)
fm3 = tk.Frame(window)
fm3.grid(row=1, column=3)



# pack(side=)
tk.Label(fm1, text=1).pack(side=tk.TOP)
tk.Label(fm1, text=2).pack(side=tk.BOTTOM)
tk.Label(fm1, text=3).pack(side=tk.RIGHT)
tk.Label(fm1, text=4).pack(side=tk.LEFT)

# grid
for i in range(4):
    for j in range(3):
        tk.Label(fm2, text=1).grid(row=i, column=j, ipadx=10, ipady=10)  # 内部扩展

# place, 指定pixel的位置
tk.Label(fm3, text=44).pack()
# tk.Label(fm3, text=4000).place(x=10, y=3, anchor="nw")  # 西北角放在指定坐标处


window.mainloop()