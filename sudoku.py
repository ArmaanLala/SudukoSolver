import tkinter as tk
import numpy as np

from tkinter import messagebox
import time
from tkinter import ttk

root = tk.Tk()
root.title("Sudoku")
done = False
canvas1 = tk.Canvas(root, width=900, height=1100)
canvas1.pack()

board = np.zeros((9, 9), dtype=int)
board = [
    [0, 0, 4, 0, 7, 0, 0, 0, 2],
    [6, 0, 2, 0, 0, 0, 0, 4, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 1, 4, 0, 3],
    [0, 0, 0, 8, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 2, 0, 4],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 5, 0, 8, 0, 0, 0, 9]]

large_font = ('Verdana', 65)
rows = []

for i in range(9):
    cols = []
    for j in range(9):
        cols.append(tk.Entry(root, width=2, font=large_font, justify=tk.CENTER))
        # cols.append(1)
        # print(len(cols))
    rows.append(cols)

# print (rows)

for i in range(9):
    for j in range(9):
        canvas1.create_window((i+1)*100 - 50, (j+1) *
                              100 - 50, window=rows[i][j])
        # rows[i][j].insert(0,1)


canvas1.create_line(300, 00, 300, 900)
canvas1.create_line(0, 300, 900, 300)
canvas1.create_line(600, 00, 600, 900)
canvas1.create_line(0, 600, 900, 600)


def solve():
    global done
    if (done):
        return
    if(done == False):
        for y in range(9):
            if(done == False):
                for x in range(9):
                    if (board[y][x] == 0):
                        for n in range(1, 10):
                            if(done == False):
                                if(possible(y, x, n)):
                                    board[y][x] = n
                                    solve()
                                    board[y][x] = 0
                        return
    print(board)
    done = True
    convertFinal()
    return


def possible(y, x, n):
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


def convertFirst():

    global done
    done = False
    if (conditions()):
        for i in range(9):
            for j in range(9):
                if (rows[i][j].get() == ''):
                    board[j][i] = 0
                else:
                    board[j][i] = int(rows[i][j].get())
        print(board)
        if (not checkBoard()):
            messagebox.showerror("Error", "Stupid Idiot Armaan")
            return
        print('Moving to solve')
        solve()


def convertFinal():
    for i in range(9):
        for j in range(9):
            rows[i][j].delete(0, 'end')
            if (board[j][i] != 0):
                rows[i][j].insert(0, board[j][i])


def conditions():
    for i in range(9):
        for j in range(9):
            if (len(rows[i][j].get()) > 1):
                print('Not possible')
                return False
    return True


def checkBoard():
    for i in range(9):
        for j in range(9):
            if not (checkCol(j) and checkRow(i) and checkBox(j, i)):
                return False
    return True


def checkRow(x):
    st = set()
    for i in range(9):
        if ((int(board[x][i]) in st) and not (int(board[x][i]) == 0)):
            return False
        else:
            st.add(int(board[x][i]))
    return True


def checkCol(x):
    st = set()
    for i in range(9):
        if ((int(board[i][x]) in st) and not (int(board[i][x]) == 0)):
            return False
        else:
            st.add(int(board[i][x]))
    return True


def checkBox(y, x):
    st = set()
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if ((int(board[y0 + i][x0 + j]) in st) and not(int(board[y0 + i][x0 + j]) == 0)):
                return False
            else:
                st.add(int(board[y0 + i][x0 + j]))
    return True


def checkBoardFinal():
    for i in range(9):
        for j in range(9):
            if not (checkColFinal(j) and checkRowFinal(i) and checkBoxFinal(j, i)):
                return False
    return True


def checkRowFinal(x):
    st = set()
    for i in range(9):
        if ((int(board[x][i]) in st)):
            return False
        else:
            st.add(int(board[x][i]))
    return True


def checkColFinal(x):
    st = set()
    for i in range(9):
        if ((int(board[i][x]) in st)):
            return False
        else:
            st.add(int(board[i][x]))
    return True


def checkBoxFinal(y, x):
    st = set()
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if ((int(board[y0 + i][x0 + j]) in st)):
                return False
            else:
                st.add(int(board[y0 + i][x0 + j]))
    return True


def checkFinal():
    if (conditions()):
        for i in range(9):
            for j in range(9):
                if (rows[i][j].get() == ''):
                    board[j][i] = 0
                else:
                    board[j][i] = int(rows[i][j].get())
    global labelVar
    if (checkBoardFinal()):
        labelVar.set("Solution is correct")
    else:
        labelVar.set("Bad")


def clear():
    global labelVar
    labelVar.set('')
    for i in range(9):
        for j in range(9):
            rows[i][j].delete(0, 'end')


def qu():
    exit()


labelVar = tk.StringVar()
labelVar.set('')
button1 = tk.Button(text='Solve', command=convertFirst)
button2 = tk.Button(text='Clear', command=clear)
button3 = tk.Button(text='Exit', command=qu)
button4 = tk.Button(text='Check', command=checkFinal)
button5 = tk.Button(text='Generate')
label1 = tk.Label(root, textvar=labelVar)
canvas1.create_window(450, 950, window=button1)

canvas1.create_window(600, 950, window=button2)
canvas1.create_window(300, 950, window=button3)
canvas1.create_window(300, 1000, window=button4)
canvas1.create_window(600, 1000, window=button5)
canvas1.create_window(450, 1000, window=label1)
convertFinal()
root.mainloop()
