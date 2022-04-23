from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

from attr import field


root = Tk()
root.title("Sudoku")

cell_values = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']

rw, cl = (0, 0)

cell = [[[] for i in range(9)] for j in range(9)]
cell_tmp = [[[] for i in range(9)] for j in range(9)]

for i in range(9):
    for j in range(9):
        cell_tmp[i][j] = StringVar()
        cell[i][j] = Entry(root, width=3, justify=CENTER, textvariable=cell_tmp[i][j])
        cell[i][j].grid(row=i, column=j)

        cl += 1
        if(cl>2):
            cl = 0
            rw += 1


def startBttnCmd():
    sudoku_field = [[0 for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            cell_cur = cell_tmp[i][j].get()
            if( (len(cell_cur) == 1) and (ord(cell_cur) >=49) and (ord(cell_cur) <= 57) ):
                sudoku_field[i][j] = int(cell_tmp[i][j].get())
            elif(len(cell_cur) > 1):
                messagebox.showinfo(message="Некорректный ввод")
                return 0
    
    '''sudoku_field = [[2,3,8,9,6,5,7,0,0],
                    [7,5,9,4,1,3,6,0,2],
                    [4,0,6,2,7,8,0,5,3],
                    [9,0,5,1,3,0,2,7,8],
                    [6,0,7,5,0,4,1,3,9],
                    [3,2,1,0,9,7,4,6,5],
                    [1,6,0,3,5,9,8,4,7],
                    [5,0,4,6,8,2,3,9,1],
                    [0,9,3,7,4,1,5,2,6]]'''
    '''sudoku_field = [[2,0,0,0,6,0,7,0,0],
                    [0,5,9,0,0,0,0,8,0],
                    [0,1,0,2,0,0,0,5,3],
                    [0,0,0,1,0,6,0,0,8],
                    [6,0,0,5,0,0,1,0,0],
                    [3,0,1,0,0,0,4,6,0],
                    [0,0,2,0,5,0,8,0,0],
                    [0,0,0,6,0,2,0,9,1],
                    [8,0,0,7,4,0,5,0,0]]'''
    '''sudoku_field = [[0,0,0,0,6,0,7,0,0],
                    [0,5,9,0,0,0,0,0,0],
                    [0,1,0,2,0,0,0,0,0],
                    [0,0,0,1,0,6,0,0,8],
                    [6,0,0,5,0,0,1,0,0],
                    [3,0,1,0,0,0,4,6,0],
                    [0,0,2,0,5,0,8,0,0],
                    [0,0,0,6,0,2,0,9,1],
                    [8,0,0,7,4,0,5,0,0]]'''
    sudoku_field = sudokuSolve(sudoku_field)
    for i in range(9):
        for j in range(9):
            if(sudoku_field[i][j] != 0):
                cell[i][j].delete(0, END)
                cell[i][j].insert(END, str(sudoku_field[i][j]))
    #print(sudoku_field, cell_tmp)

def sudokuSolve(sudoku_field):
    condition_save = []
    i = 0
    while(i < 9):
        j = 0
        while(j < 9):
            if(sudoku_field[i][j] == 0):
                pssbl_values = list(set.intersection(set(colCheck(j, sudoku_field)),set(rawCheck(i, sudoku_field)), set(squareCheck(j,i,sudoku_field))))
                '''print(condition_save)
                    messagebox.showinfo(message="Некорректный ввод")
                    return sudoku_field'''
                #print(pssbl_values, set(colCheck(j, sudoku_field)),set(rawCheck(i, sudoku_field)), set(squareCheck(j,i,sudoku_field)))
                if(len(pssbl_values) == 1):
                    sudoku_field[i][j] = pssbl_values[0]
                elif(len(pssbl_values) > 1):
                    field_copy = []
                    for k in range(9):
                        field_copy.append(sudoku_field[k][:])
                    condition_save.append([field_copy, pssbl_values[1:], [i,j]])
                    sudoku_field[i][j] = pssbl_values[0]
                else:
                    try:
                        sudoku_field = condition_save[-1][0]
                    except IndexError:
                        messagebox.showinfo(message="Некорректный ввод")
                        return sudoku_field
                    pssbl_values = condition_save[-1][1]
                    i, j = condition_save[-1][2]
                    if(j == 8):
                        print(8)
                    sudoku_field[i][j] = pssbl_values[0]
                    condition_save[-1][1] = pssbl_values[1:]
                    if(len(condition_save[-1][1]) == 0):
                        condition_save.pop(-1)
            j += 1
        i += 1

    return sudoku_field

def colCheck(col_id, sudoku_field):
    values = [0 for i in range(10)]
    for i in range(9):
        if(sudoku_field[i][col_id] == 0):
            #print(i,col_id)
            continue
        values[sudoku_field[i][col_id]] += 1
        #print(values)
        if(values[sudoku_field[i][col_id]] > 1):
            #print('col')
            return []
    pssbl_values = []
    for i in range(1, 10):
        if(values[i] == 0):
            pssbl_values.append(i)
    
    return pssbl_values

def rawCheck(raw_id, sudoku_field):
    values = [0 for i in range(10)]
    for i in range(9):
        if(sudoku_field[raw_id][i] == 0):
            continue
        values[sudoku_field[raw_id][i]] += 1
        if(values[sudoku_field[raw_id][i]] > 1):
            #print('raw')
            return []
    pssbl_values = []
    for i in range(1, 10):
        if(values[i] == 0):
            pssbl_values.append(i)
    
    return pssbl_values

def squareCheck(col_id, raw_id, sudoku_field):
    values = [0 for i in range(10)]
    col_start = 3 * (col_id // 3)
    raw_start = 3 * (raw_id // 3)
    for i in range(3):
        for j in range(3):
            if(sudoku_field[raw_start + i][col_start + j] == 0):
                continue
            values[sudoku_field[raw_start + i][col_start + j]] += 1
            if(values[sudoku_field[raw_start + i][col_start + j]] > 1):
                #print('sqr', values)
                return []
    pssbl_values = []
    for i in range(1, 10):
        if(values[i] == 0):
            pssbl_values.append(i)
    
    return pssbl_values

def notEmptyCellCnt(sudoku_field):
    cnt = 0
    for i in range(9):
        for j in range(9):
            if(sudoku_field[i][j] != 0):
                cnt += 1
    
    return cnt


start_bttn = Button(root, width = 9, text="start", command=startBttnCmd)
start_bttn.grid(row=9, column=3, columnspan=3)

root.mainloop()