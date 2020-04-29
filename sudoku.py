import tkinter as tk
import numpy as np

from tkinter import messagebox
import time
from tkinter import ttk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 900, height = 1000)
canvas1.pack()

board = np.zeros((9,9), dtype=int)
board = [[5 ,3, 4, 6, 7, 8, 9, 1, 2],
 [6, 7, 2, 1, 9, 5, 3, 4, 8],
 [1 ,9, 8, 3, 4, 2, 5, 6, 7],
 [8 ,5 ,9 ,7 ,6 ,1 ,4 ,2 ,3],
 [4 ,2 ,6 ,8 ,5, 3, 7, 9, 1],
 [7 ,1 ,3 ,9 ,2 ,4 ,8 ,5, 6],
 [9, 6, 1, 5, 3, 7, 2, 8, 4],
 [2, 8, 7, 4, 1, 9, 6, 3, 5],
 [3, 4, 5, 2, 8, 6, 1, 7, 9]]

large_font = ('Verdana',65)
rows = []

for i in range(9):
    cols=[]
    for j in range(9):
        cols.append(tk.Entry(root, width=2,font=large_font, justify = tk.CENTER))
        # cols.append(1)
        # print(len(cols))
    rows.append(cols)

# print (rows)

for i in range(9):
    for j in range(9):
        canvas1.create_window((i+1)*100 - 50, (j+1)*100 - 50 , window=rows[i][j])
        # rows[i][j].insert(0,1)


canvas1.create_line(300,00,300,900)

canvas1.create_line(0,300,900,300)

canvas1.create_line(600,00,600,900)

canvas1.create_line(0,600,900,600)

recur = 0
count =0
unkown = 0 


def solve ():
    global count
    if (count == 1):
        convert2()
        return
    global recur
    
    for y in range(9):
        for x in range(9):
            if (board[y][x] == 0):
                for n in range (1,10):
                    if(possible(y,x,n)):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return 
    print(board)
    count = count + 1
    if (count == 1):
        convert2()
        return


def possible(y,x,n):
    for i in range(9):
        if board[y][i] == n:
            return False
    for i in range(9):
        if board[i][x] == n:
            return False
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if board[y0 + i][x0 + j] == n:
                return False
    return True

def convert1 () :
    if (conditions()):
        for i in range(9):
            for j in range(9):
                if (rows[i][j].get() == ''):
                    unkown = unkown +1
                    board[j][i] = 0
                else:
                    board[j][i] = int(rows[i][j].get())
        print(board)
        if (unkown > (81-17)):
            messagebox.showerror("Error", "Error message")
            else:
        print('Moving to solve')
        solve()
        

def convert2() :
    global count
    for i in range(9):
        for j in range(9):
            # board[j][i] = int(rows[i][j].get())
            rows[i][j].delete(0,'end')
            rows[i][j].insert(0,board[j][i])
    count = 0

def conditions():
    for i in range(9):
        for j in range(9):
            if (len(rows[i][j].get()) > 1):
                print('Not possible')
                return False
    return True

def clear():
    for i in range(9):
        for j in range(9):
            # board[j][i] = int(rows[i][j].get())
            rows[i][j].delete(0,'end')
def qu () :
    exit()
    
button1 = tk.Button(text='Solve', command=convert1)
button2 = tk.Button(text='Clear', command=clear)
button3 = tk.Button(text='Exit', command=qu)
canvas1.create_window(450,950, window=button1)

canvas1.create_window(600,950, window=button2)

canvas1.create_window(300,950, window=button3)
convert2()
root.mainloop()