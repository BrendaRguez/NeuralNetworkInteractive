import tensorflow as tf
from tkinter import *
import numpy as np
#import matplotlib.pyplot as plt

#LOAD A NEW MODEL (UNO PROPIO)
new_model = tf.keras.models.load_model("num_reader_mask.keras")


class canvasByPixel:
    def __init__(self,numberPixelArt,canvasPixelSize, master):
        
        self.numberPixelArt = numberPixelArt
        self.canvasPixelSize = canvasPixelSize
        self.PixelArray = np.zeros((numberPixelArt, numberPixelArt))
        self.PincelSize = 30

        # Frame to hold the button
        self.button_frame = Frame(master)
        self.button_frame.pack(side=TOP, fill=X)

        # Clear Canvas button
        self.button = Button(self.button_frame, text="Clear Canvas", command=self.clear_canvas)
        self.button.pack(side=TOP)

        self.w = Canvas(master, 
           width=numberPixelArt*canvasPixelSize,
           height=numberPixelArt*canvasPixelSize)
        self.w.pack()

        # self.button = Button(self.w, text="Clear Canvas", command=self.clear_canvas)
        # self.button.pack()

        self.default_canvas()

        self.w.bind( "<B1-Motion>", self.MotionPaint)
        self.w.bind( "<Button-1>", self.MotionPaint)

        
    
    def clear_canvas(self):
        self.w.delete("all")
        self.default_canvas()
        self.PixelArray = np.zeros((numberPixelArt, numberPixelArt))

    def default_canvas(self):
        for i in range(self.numberPixelArt*self.numberPixelArt-1):
            for j in range(self.numberPixelArt*self.numberPixelArt-1):
                x1 = i * self.canvasPixelSize
                y1 = j * self.canvasPixelSize
                x2 = x1 + self.canvasPixelSize
                y2 = y1 + self.canvasPixelSize
                self.w.create_rectangle(x1,y1,x2,y2,outline="#476042", fill="white")

    def MotionPaint(self,event):
        #print(event.x//self.canvasPixelSize,event.y//self.canvasPixelSize)
        array_x = event.x // self.canvasPixelSize
        array_y = event.y //self.canvasPixelSize
        x1 = array_x * self.canvasPixelSize
        y1 = array_y * self.canvasPixelSize
        x2 = x1 + self.PincelSize
        y2 = y1 + self.PincelSize

        self.w.create_rectangle(x1,y1,x2,y2,outline="green", fill="green")
        pincelsize = self.PincelSize//canvasPixelSize
        #self.PixelArray[event.y//self.canvasPixelSize,event.x//self.canvasPixelSize] = 1  #Change this for the bigger pencil
        self.PixelArray[
            array_y:array_y+pincelsize,
            array_x:array_x+pincelsize] = 1  #Change this for the bigger pencil

        image = np.expand_dims(self.PixelArray, axis=0) #Reshape to adjust to the input of the model
        predictions = new_model.predict(image)
        percentages = np.round(predictions[0] * 100).astype(int)

        print("Prediction:       ",np.argmax(predictions[0]),"percentages by digit: ",percentages)
       # print(self.PixelArray.tolist())


if __name__ == "__main__":
    numberPixelArt = 28 #Numbers of rectangles that I want  n X n
    canvasPixelSize = 10 #Pixel size of every rectangle
    master = Tk()
    root = canvasByPixel(numberPixelArt,canvasPixelSize,master=master)
    master.mainloop()



