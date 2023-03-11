# Digit Sayer
This is a Python application that can recognize handwritten digits using a neural network trained on the MNIST dataset. The application has two main components:

`train.py`: A script for training the neural network on the MNIST dataset using Keras.

`main.py`: A GUI application that allows the user to draw a digit on a canvas and get a prediction of the digit from the neural network.

## Getting Started
To use this application, you will need Python 3 and the following Python packages:

--> Keras

--> TensorFlow

--> NumPy

--> Pillow

--> Tkinter

You can install these packages using the following command:

`pip install -r requirements.txt`

## Training the Model

To train the neural network, run the train.py script:

`python train.py`

This will train the neural network on the MNIST dataset using Keras and save the trained model to a file called my_model.h5.

Note that the training process may take several minutes to complete, depending on your hardware.

You can change the parameters to meet your requirements.
Using the code, I was able to attain `accuracy: 0.9981` and the model predicted my handwritten digits pretty efficiently. 

## Using the GUI Application

To use the GUI application, run the `main.py` script:

`python main.py`

This will open a window with a canvas where you can draw a digit using your mouse. Once you're satisfied with your drawing, click the **Predict** button to get a prediction of the digit from the neural network.

The predicted digit will be displayed on the canvas, along with the probability of the prediction.
