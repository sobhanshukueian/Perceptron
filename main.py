from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from functools import partial
import tkinter as tk
import json


def perceptron(train, entry, learning_rate, bios, theta):
    weight = []
    initial_weights = (open("./weights.txt", "r+")).read()

    if len(initial_weights) == 0 or train:
        weights = [0] * 26

        delete_weights =  (open("./weights.txt", "a+")).truncate(0)

        with open('./dataset.txt', 'r') as filehandle:
            dataset = json.load(filehandle)

        for input in dataset:
            for i in range(len(input) - 2):
                y_ni = (input[i] * weights[i]) + bios
                if y_ni >= 0:
                    y = 1
                else:
                    y = -1

                if y != input[-1]:
                    weights[i] += learning_rate * input[-1] * input[i]
                    bios += learning_rate * input[-1]
        with open('./weights.txt', 'w') as filehandle:
            json.dump(weights, filehandle)
        if train != True:
            for i in range(24):
                total += (weights[i] * entry[i]) + bios  
            if total >= theta:
                messagebox.showwarning("Success", "Character is X")
            elif total < -1*theta:
                messagebox.showwarning("Success", "Character is O")
            else:
                messagebox.showwarning("Error", "Try again")

    else:
        total = 0
        with open('./weights.txt', 'r') as filehandle:
            weight = json.load(filehandle)
        for i in range(24):
            x = (weight[i] * entry[i]) + bios 
            total += x
        if total >= theta:
            messagebox.showwarning("Success", "Character is X")
        elif total < -1*theta:
            messagebox.showwarning("Success", "Character is O")
        else:
            messagebox.showwarning("Error", "Try again")

def get_data(data,  n):
    datas = data[:]
    if(n == 1):
        perceptron(False, data,1, 0, 0.2)
    elif var.get().upper() == "X":
        datas.append(1)
        with open('./dataset.txt', 'r+') as filehandle:
            dataset_data = json.load(filehandle)
            dataset_data.append(datas)
            filehandle.seek(0)
            json.dump(dataset_data, filehandle)
        perceptron(True, datas, 1,0, 0.2)
        messagebox.showwarning("Success", "Saved data successfully")

    elif var.get().upper() == "O":
        datas.append(-1)
        with open('./dataset.txt', 'r+') as filehandle:
            dataset_data = json.load(filehandle)
            dataset_data.append(datas)
            filehandle.seek(0)
            json.dump(dataset_data, filehandle)
        perceptron(True, datas,1, 0, 0.2)
        messagebox.showwarning("Success", "Saved data successfully")

    else:
        messagebox.showwarning("Error", "Invalid Data")


gui = Tk()
gui.geometry("375x375")
var = StringVar()


def select_button(widget, n, arr):
    m = widget['text']
    if(arr[m] == 1):
        widget['bg'] = 'black'
        arr[m] = -1
    else:
        widget['bg'] = 'white'
        arr[m] = 1


arr = [-1] * 25
for i in range(25):
    btn = tk.Button(gui, text=i, bg="black", height=5, width=10,)
    btn.config(command=lambda arg=btn: select_button(arg, i, arr))
    btn.grid(row=i // 5, column=i % 5, sticky='w')

# Inorder to make GUI responsive
n_rows = 5
n_columns = 5
for i in range(n_rows):
    for j in range(n_columns):
        gui.grid_rowconfigure(i, weight=1)
        gui.grid_columnconfigure(j, weight=1)

entry1 = Entry(gui, text="Enter Character", textvariable=var,
               width=8, background="gray")
entry1.grid(row=7, column=0)

button1 = Button(gui, text="Train", command=partial(get_data, arr, 0),
                 width=9, background="gray")
button1.grid(row=7, column=1)


button1 = Button(gui, text="Predict", command=partial(get_data, arr, 1),
                 width=9, background="gray")
button1.grid(row=7, column=3)

mainloop()
