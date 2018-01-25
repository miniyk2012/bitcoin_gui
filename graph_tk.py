import matplotlib
matplotlib.use("TkAgg")
import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
import numpy as np
import json
import urllib

style.use('ggplot')

LARGE_FONT = ("Verdana", 12)

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)


def animate(i):
    pull_data = open('sampleData.txt', 'r').read()
    data_list = pull_data.split('\n')
    x_list = []
    y_list = []
    for line in data_list:
        if len(line) > 0:
            x, y = line.split(',')
            x_list.append(int(x))
            y_list.append(int(y))
    a.clear()
    a.plot(x_list, y_list)
    print('hey, guys')


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, "favicon.ico")
        tk.Tk.wm_title(self, "Sea of BTC Client")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, BTCe_Page):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""ALPHA Bitcoin trading application
        use at your own risk. There is no promise
        of warranty."""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Agree", command=lambda: controller.show_frame(BTCe_Page))
        button.pack()

        button2 = ttk.Button(self, text="Disagree", command=quit)
        button2.pack()


class BTCe_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Three!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


if __name__ == '__main__':
    app = SeaofBTCapp()
    ani = animation.FuncAnimation(f, animate, interval=1000)  # 每秒调用animate()一次
    app.mainloop()
