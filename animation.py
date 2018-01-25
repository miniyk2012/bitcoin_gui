from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,    NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use("ggplot")


class Application(Frame):
    """A GUI app with some buttons."""

    def __init__(self, master):
        """ Initialze frame"""
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks=0 #count the number of button click
        self.create_widgets()

    def create_widgets(self):
        """Create button which displays number of clicks."""

        #Button1
        self.button1 = Button(self)
        self.button1 ["text"]="in"
        self.button1["command"] = self.update_news
        self.button1.grid()

    def update_news(self):
        toplevel = Toplevel()

        self.f = Figure(figsize = (5,5), dpi = 100)
        self.a = self.f.add_subplot(111)


        self.canvas = FigureCanvasTkAgg(self.f,toplevel)
        self.canvas.show()
        self.canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2TkAgg(self.canvas,toplevel)
        toolbar.update()
        self.canvas._tkcanvas.pack()

        self.ani = animation.FuncAnimation(app.f, app.animate, frames=100,interval=100)

    def animate(self,i):
        """
        pullData = open ("sampleData.txt","r").read()
        datalist = pullData.split('\n')
        xList = []
        yList = []
        for eachLine in dataList:
            if len (eachLine)>1:
                x,y=eachLine.split(',')
                xList.append(int (x))
                yList.append(int (y))
        """
        xList = np.arange(i+1)
        yList = np.sin(xList/10.)
        self.a.clear()
        self.a.plot(xList,yList)


#Building the window
root = Tk()
root.title("Buttons")
root.geometry("200x300")

app = Application(root)

#MainLoop
root.mainloop()