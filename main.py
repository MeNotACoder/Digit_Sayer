import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas
from tkinter import Button
from PIL import Image, ImageDraw
import numpy as np
from keras.models import load_model

# Load the trained model
model = load_model('mnist_model.h5')

# Create the GUI
class App:
    def __init__(self, master):
        self.master = master
        self.master.title('.')
        self.canvas = Canvas(self.master, width=300, height=300, bg='white')
        self.canvas.pack(expand='YES', fill='both')
        self.canvas.bind('<B1-Motion>', self.draw)
        self.button_clear = Button(text='Clear', command=self.clear)
        self.button_clear.pack(side='left')
        self.button_predict = Button(text='Predict', command=self.predict)
        self.button_predict.pack(side='right')
        self.image = Image.new('L', (300, 300), 0)
        self.draw = ImageDraw.Draw(self.image)

    def clear(self):
        self.canvas.delete('all')
        self.image = Image.new('L', (300, 300), 0)
        self.draw = ImageDraw.Draw(self.image)

    def draw(self, event):
        x, y = event.x, event.y
        r = 10
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill='black')
        self.draw.ellipse((x-r, y-r, x+r, y+r), fill='white')

    def predict(self):
        digit = self.image.resize((28, 28))
        digit_array = np.array(digit)
        digit_array = digit_array.reshape(1, 28, 28, 1)
        digit_array = digit_array.astype('float32') / 255.0
        prediction = model.predict(digit_array)
        predicted_digit = np.argmax(prediction)
        messagebox.showinfo('Prediction', f'The predicted digit is {predicted_digit}')

root = tk.Tk()
app = App(root)
root.mainloop()
