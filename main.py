import tensorflow as tf
from tkinter import *

#LOAD A NEW MODEL (UNO PROPIO)
new_model = tf.keras.models.load_model("num_reader.keras")

#PREDICTIONS
##---> AL FINAL predictions = new_model.predict(x_test)

numberPixelArt = 28 #Numbers of rectangles that I want
canvasPixelSize = 10 #Pixel size of every rectangle

def default_canvas(canvas, line_distance):
   for i in range(numberPixelArt*numberPixelArt-1):
      for j in range(numberPixelArt*numberPixelArt-1):
        x1 = i * canvasPixelSize
        y1 = j * canvasPixelSize
        x2 = x1 + canvasPixelSize
        y2 = y1 + canvasPixelSize
        canvas.create_rectangle(x1,y1,x2,y2,outline="#476042", fill="white")

def MotionPaint(event):
   print(event.x//canvasPixelSize,event.y//canvasPixelSize)
   x1 = event.x //canvasPixelSize * canvasPixelSize
   y1 = event.y //canvasPixelSize * canvasPixelSize
   x2 = x1 + 10
   y2 = y1 + 10

   w.create_rectangle(x1,y1,x2,y2,outline="#476042", fill="green")
#    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
#    x2, y2 = ( event.x + 1 ), ( event.y + 1 )
#    w.create_oval( x1, y1, x2, y2, fill = python_green )

master = Tk()
global w
w = Canvas(master, 
           width=numberPixelArt*canvasPixelSize,
           height=numberPixelArt*canvasPixelSize)
w.pack()

w.bind( "<B1-Motion>", MotionPaint)

default_canvas(w,10)

master.mainloop()
