from operator import index, le
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


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
                    [8,0,0,7,4,0,5,0,0]]
    sudoku_field = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]]'''
    # sudoku_field = [[0,6,0,0,0,0,7,0,0],
    #                 [8,0,9,0,6,0,5,0,0],
    #                 [2,4,5,0,1,0,8,0,0],
    #                 [0,0,0,5,0,0,0,0,4],
    #                 [0,5,4,0,0,0,6,9,0],
    #                 [3,0,0,0,0,6,0,0,0],
    #                 [0,0,7,0,5,0,1,2,6],
    #                 [0,0,2,0,7,0,4,0,5],
    #                 [0,0,1,0,0,0,0,7,0]]
    # sudoku_field = [[6,0,0,0,5,7,4,9,0],
    #                 [0,0,0,0,9,0,5,0,6],
    #                 [0,9,5,0,0,0,0,0,0],
    #                 [0,0,0,0,0,0,0,4,2],
    #                 [0,5,0,4,0,6,0,8,0],
    #                 [8,3,0,0,0,0,0,0,0],
    #                 [0,0,0,0,0,0,1,2,0],
    #                 [9,0,3,0,1,0,0,0,0],
    #                 [0,1,2,7,8,0,0,0,3]]
    sudoku_field = sudokuSolver(sudoku_field)
    for i in range(9):
        for j in range(9):
            if(sudoku_field[i][j] != 0):
                cell[i][j].delete(0, END)
                cell[i][j].insert(END, str(sudoku_field[i][j]))
    #print(sudoku_field, cell_tmp)

'''def sudokuSolve(sudoku_field):
    condition_save = []
    i = 0
    while(i < 9):
        j = 0
        while(j < 9):
            if(sudoku_field[i][j] == 0):
                pssbl_values = list(set.intersection(set(colCheck(j, sudoku_field)),set(rawCheck(i, sudoku_field)), set(squareCheck(j,i,sudoku_field))))
                #print(condition_save)
                #messagebox.showinfo(message="Некорректный ввод")
                #return sudoku_field
                #print(pssbl_values, set(colCheck(j, sudoku_field)),set(rawCheck(i, sudoku_field)), set(squareCheck(j,i,sudoku_field)))
                if(len(pssbl_values) == 1):
                    print(pssbl_values,i,j)
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
                        #print(condition_save)
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

    return sudoku_field'''

def sudokuSolver(sudoku_field):
    single_solution = False
    possible_vars = [[[] for j in range(9)] for i in range(9)]
    possible_amount = [[0 for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            if(sudoku_field[i][j] == 0):
                pssbl_values = list(set.intersection(set(colCheck(j, sudoku_field)),set(rawCheck(i, sudoku_field)), set(squareCheck(j,i,sudoku_field))))
                possible_amount[i][j] = len(pssbl_values)
                if(len(pssbl_values) == 1):
                    single_solution = True
                    sudoku_field[i][j] = pssbl_values[0]
                    possible_vars[i][j] = []
                    possible_amount[i][j] = 0
                else:
                    possible_vars[i][j] = pssbl_values
    if(not(zeroCellZeroVars(sudoku_field, possible_amount))):
        messagebox.showinfo(message="Некорректный ввод")
        return sudoku_field

    condition_save = []

    #condition_save.append([field_copy(sudoku_field), minVarsCell(possible_amount, sudoku_field), field_copy(possible_amount), field_copy(possible_vars)])
    i, j = 0, 0
    while(i < 9):
        j = 0
        while(j < 9):
            # if(sudoku_field[1][0] == 7):
            #     print(i,j)
            #     print(sudoku_field)
            if(sudoku_field[i][j] == 0):
                pssbl_values = list(set.intersection(set(colCheck(j, sudoku_field)),set(rawCheck(i, sudoku_field)), set(squareCheck(j,i,sudoku_field))))
                # if(sudoku_field[1][0] == 7):
                #     print(i,j)
                '''if(i == 0 and j == 3):
                    print(condition_save)
                if(i == 1 and j == 1):
                    print(condition_save)
                    print(pssbl_values)
                    print(sudoku_field)
                print(i,j)
                print(sudoku_field)'''
                if(len(pssbl_values) == 1):
                    # if(i == 1 and j == 2):
                    #     print(i,j)
                    #     print(sudoku_field)
                    #     print(pssbl_values)
                    sudoku_field[i][j] = pssbl_values[0]
                elif(len(pssbl_values) > 1):
                    # if(i == 1 and j == 2):
                    #     print(i,j)
                    #     print(sudoku_field)
                    #     print(pssbl_values)
                    condition_save.append([])
                    condition_save[-1] = [field_copy(sudoku_field), [i,j], len(pssbl_values) - 1, pssbl_values[1:]]
                    sudoku_field[i][j] = pssbl_values[0]
                elif(len(pssbl_values) == 0):
                    # if(i == 2 and j == 5):
                    #     print(i,j)
                    #     print(sudoku_field)
                    #     print(condition_save)
                    #     print("**********")
                    while(condition_save[-1][2] == 0):
                        '''print(condition_save)
                        print('---------')'''
                        del condition_save[-1]
                    i,j = condition_save[-1][1]
                    sudoku_field = field_copy(condition_save[-1][0])
                    sudoku_field[i][j] = condition_save[-1][3][0]
                    condition_save[-1][3] = condition_save[-1][3][1:]
                    condition_save[-1][2] -= 1
                    if(condition_save[-1][2] == 0):
                        del condition_save[-1]
            j += 1
        i += 1

    return sudoku_field   



def prioritySolver(sudoku_field):
    single_solution = False
    possible_vars = [[[] for j in range(9)] for i in range(9)]
    possible_amount = [[0 for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            if(sudoku_field[i][j] == 0):
                pssbl_values = list(set.intersection(set(colCheck(j, sudoku_field)),set(rawCheck(i, sudoku_field)), set(squareCheck(j,i,sudoku_field))))
                possible_amount[i][j] = len(pssbl_values)
                if(len(pssbl_values) == 1):
                    single_solution = True
                    sudoku_field[i][j] = pssbl_values[0]
                    possible_vars[i][j] = []
                    possible_amount[i][j] = 0
                else:
                    possible_vars[i][j] = pssbl_values
    if(not(zeroCellZeroVars(sudoku_field, possible_amount))):
        messagebox.showinfo(message="Некорректный ввод")
        return sudoku_field

    condition_save = []

    if(single_solution):
        sudoku_field, possible_vars, possible_amount = singleSolution(sudoku_field, possible_vars, possible_amount)  

    condition_save.append([field_copy(sudoku_field), minVarsCell(possible_amount, sudoku_field), field_copy(possible_amount), field_copy(possible_vars)])
    
    while(len(condition_save) > 0):
        while(zeroCellZeroVars(sudoku_field, possible_amount)):
            '''if(single_solution):
                sudoku_field, possible_vars, possible_amount = singleSolution(sudoku_field, possible_vars, possible_amount)
                print('first')
                print(sudoku_field)
            else:'''
            #print('second')
            condition_save.append([field_copy(sudoku_field)])
            save_i, save_j ,sudoku_field, possible_vars, possible_amount = notSingleSolution(sudoku_field, possible_vars, possible_amount)
            print("**\n", save_i, save_j, "\n**")
            #single_solution = singleSolutionCheck(possible_amount)
            condition_save[-1].append([save_i,save_j])
            condition_save[-1].append(field_copy(possible_amount)) 
            condition_save[-1].append(field_copy(possible_vars))
            print(sudoku_field)
            print(condition_save[-1][0])
            #print(condition_save[-1][1])
            #print(condition_save[-1][2])
            #print(condition_save[-1][3])
            print('------')
            for i in range(9):
                for j in range(9):
                    if(sudoku_field[i][j] == 0):
                        pssbl_values = list(set.intersection(set(colCheck(j, sudoku_field)),set(rawCheck(i, sudoku_field)), set(squareCheck(j,i,sudoku_field))))
                        possible_amount[i][j] = len(pssbl_values)
                        if(len(pssbl_values) == 1):
                            single_solution = True
                            sudoku_field[i][j] = pssbl_values[0]
                            possible_vars[i][j] = []
                            possible_amount[i][j] = 0
                        else:
                            possible_vars[i][j] = pssbl_values
        '''if(sudoku_field[0][1] == 8):
            print(sudoku_field)
            print(condition_save[-1][0])
            print(condition_save[-1][1])
            print(condition_save[-1][2])
            print(condition_save[-1][3])
            print('------')'''
        if(notEmptyCellCnt(sudoku_field) == 81):
            return sudoku_field

        #print(condition_save[-1])
        cell_i, cell_j = condition_save[-1][1][0], condition_save[-1][1][1]
        #print(cell_i, cell_j)
        #print('----------')
        if(possible_amount[cell_i][cell_j] > 0):
            #print(cell_i, cell_j, condition_save[-1][-2])
            sudoku_field = field_copy(condition_save[-1][0])
            possible_vars = field_copy(condition_save[-1][-1])
            sudoku_field[cell_i][cell_j] = possible_vars[cell_i][cell_j][0]
            possible_amount = field_copy(condition_save[-1][-2])
            possible_amount[cell_i][cell_j] -= 1
            possible_vars[cell_i][cell_j] = possible_vars[cell_i][cell_j][1:]
        else:
            while(possible_amount[cell_i][cell_j] == 0 and len(condition_save) > 0):
                #print(cell_i, cell_j, condition_save[-1][-2])
                cell_i, cell_j = condition_save[-1][1][0], condition_save[-1][1][1]
                #print(cell_i, cell_j, condition_save[-1])
                #print(condition_save[-1][2])
                if(len(condition_save) == 1):
                    copy_cs = condition_save[:]
                del condition_save[-1]
                #sudoku_field = condition_save[-1][0]
                #sudoku_field[cell_i][cell_j] == possible_vars[cell_i][cell_j][0]
                #possible_amount[cell_i][cell_j] -= 1
                #possible_vars[cell_i][cell_j] = possible_vars[cell_i][cell_j][1:]
            if(len(condition_save) == 0):
                condition_save.append(copy_cs[0])
                #print("=======\n",copy_cs, "\n=======")
                #print(condition_save[-1][0])
            elif(possible_amount[cell_i][cell_j] == 0):
                print(possible_amount, cell_i, cell_j)
                messagebox.showinfo(message="Некорректный ввод")
                return sudoku_field
                '''sudoku_field = condition_save[-1][0]
                possible_vars = condition_save[-1][-1]
                sudoku_field[cell_i][cell_j] = possible_vars[cell_i][cell_j][0]
                possible_amount = condition_save[-1][-2]
                possible_amount[cell_i][cell_j] -= 1
                possible_vars[cell_i][cell_j] = possible_vars[cell_i][cell_j][1:]'''
                

    print(len(condition_save))
    return(sudoku_field)


def field_copy(sudoku_field):
    field_copy = []
    for k in range(len(sudoku_field)):
        field_copy.append(sudoku_field[k][:])
    return field_copy

def zeroCellZeroVars(suddoku_field, possible_amount):
    for i in range(9):
        for j in range(9):
            if(suddoku_field[i][j] == 0 and possible_amount[i][j] == 0):
                '''print(i,j)
                print(suddoku_field)
                print(possible_amount)'''
                return False
    return True

def singleSolutionCheck(possible_amount):
    for i in range(9):
        for j in range(9):
            if(possible_amount[i][j] == 1):
                return True
    
    return False

def singleSolution(sudoku_field, possible_vars, possible_amount, single_solution=True):
    while(single_solution):
        single_solution = False
        for i in range(9):
            for j in range(9):
                if(sudoku_field[i][j] == 0):
                    if(possible_amount[i][j] == 1):
                        sudoku_field[i][j] = possible_vars[i][j][0]
                        del possible_vars[i][j][-1]
                        possible_amount[i][j] -= 1
                    else:
                        pssbl_values = list(set.intersection(set(colCheck(j, sudoku_field)),set(rawCheck(i, sudoku_field)), set(squareCheck(j,i,sudoku_field))))
                        possible_amount[i][j] = len(pssbl_values)
                        if(len(pssbl_values) == 1):
                            single_solution = True
                        possible_vars[i][j] = pssbl_values
    

    return(sudoku_field, possible_vars, possible_amount)

def notSingleSolution(sudoku_field, possible_vars, possible_amount):
    min_vars_id = minVarsCell(possible_amount, sudoku_field)
    min_i, min_j = min_vars_id[0], min_vars_id[1]
    sudoku_field[min_i][min_j] = possible_vars[min_i][min_j][0]
    possible_amount[min_i][min_j] -= 1
    possible_vars[min_i][min_j] = possible_vars[min_i][min_j][1:]
    #print(min_i, min_j, sudoku_field, possible_vars, possible_amount)

    return (min_i, min_j, sudoku_field, possible_vars, possible_amount)
    

def minVarsCell(possible_amount, sudoku_field):
    m = 10
    min_id = [-1,-1]
    for i in range(9):
        for j in range(9):
            if(possible_amount[i][j] != 0 and possible_amount[i][j] < m and sudoku_field[i][j] == 0):
                m = possible_amount[i][j]
                min_id = [i,j]

    return min_id

def notZeroPossibleVars(possible_amount):
    for i in range(9):
        for j in range(9):
            if(possible_amount[i][j] != 0):
                return True
    
    return(False)

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