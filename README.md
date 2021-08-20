# Perceptron
Perceptron is a single layer neural network.Perceptron Learning Algorithm, originally proposed by Frank Rosenblatt in 1943, later refined and carefully analyzed by Minsky and Papert in 1969.

![4](https://user-images.githubusercontent.com/47561760/130283139-314cf10f-df33-43c8-ac07-b431f994371b.png)

# Architecture
The perceptron works on below simple steps:

a. All the inputs x are multiplied with their weights w (Initialize the weights to 0 or small random numbers).

b. Add all the multiplied values and call them Weighted Sum.

c. Apply that weighted sum to the correct Activation Function(Ex.Unit Step Activation Function).

d. Update weights in each iteration

# How Code Works?
There are several examples for perceptron implementation that here I've chosen XO prediction in python which includes perceptron() function that performs perceptron algorithm like discussed above and getData() function for getting data and save it in dataset.txt file for training adaline weights. We store adaline weights in weights.txt file and use tkinter for GUI.
