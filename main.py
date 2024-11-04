import tensorflow as tf
from tkinter import *

#LOAD A NEW MODEL (UNO PROPIO)
new_model = tf.keras.models.load_model("num_reader.keras")

#PREDICTIONS
##---> AL FINAL predictions = new_model.predict(x_test)

class canvasByPixel:
   
    def __init__(self,numberPixelArt,canvasPixelSize, master):
        self.numberPixelArt = numberPixelArt
        self.canvasPixelSize = canvasPixelSize
        self.w = Canvas(master, 
           width=numberPixelArt*canvasPixelSize,
           height=numberPixelArt*canvasPixelSize)
        self.w.pack()

        self.default_canvas()

        self.w.bind( "<B1-Motion>", self.MotionPaint)
        self.w.bind( "<Button-1>", self.MotionPaint)
        
    def default_canvas(self):
        for i in range(self.numberPixelArt*self.numberPixelArt-1):
            for j in range(self.numberPixelArt*self.numberPixelArt-1):
                x1 = i * self.canvasPixelSize
                y1 = j * self.canvasPixelSize
                x2 = x1 + self.canvasPixelSize
                y2 = y1 + self.canvasPixelSize
                self.w.create_rectangle(x1,y1,x2,y2,outline="#476042", fill="white")

    def MotionPaint(self,event):
        print(event.x//self.canvasPixelSize,event.y//self.canvasPixelSize)

        x1 = event.x // self.canvasPixelSize * self.canvasPixelSize
        y1 = event.y //self.canvasPixelSize * self.canvasPixelSize
        x2 = x1 + 10
        y2 = y1 + 10

        self.w.create_rectangle(x1,y1,x2,y2,outline="#476042", fill="green")
    #    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
    #    x2, y2 = ( event.x + 1 ), ( event.y + 1 )
    #    w.create_oval( x1, y1, x2, y2, fill = python_green )



if __name__ == "__main__":
    numberPixelArt = 28 #Numbers of rectangles that I want
    canvasPixelSize = 10 #Pixel size of every rectangle
    master = Tk()
    root = canvasByPixel(numberPixelArt,canvasPixelSize,master=master)
    master.mainloop()
