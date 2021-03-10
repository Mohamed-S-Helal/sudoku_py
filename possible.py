
# parse array of 81 into 9 rows:ax, colums:ay and blocks:az
def parse(a):
    ax = [a[n:n+9] for n in range(0,81,9)]
    ay = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            ay[i][j] = ax[j][i]
    az = [[0 for i in range(9)] for j in range(9)]
    l1 = ax[0]+ax[3]+ax[6]; l2 = ax[1]+ax[4]+ax[7]; l3 = ax[2]+ax[5]+ax[8]
    for i in range(9):
        n = i*3
        az[i] = l1[n:n+3]+l2[n:n+3]+l3[n:n+3]
    return ax, ay, az

############################################

# check if number:n is possible to be put in index:index of array:arr by checking any similar number in the row, column or block containing this index
def possible(arr, n, index):
    if n in arr:
        a = list(range(81)); ai = parse(a); an = parse(arr)
        for i in ai: 
            index1 = ai.index(i) # ax/y/z
            for i1 in i: 
                index2 = i.index(i1)  # one element from ax/y/z
                if index in i1: 
                    if n in an[index1][index2]:
                        return False
    return True

###########################################

# FinalSolve solve the zero cells of array:arr and returns one solution or two if more were available
def Fsolve(arr):
    x = arr.copy()
    y = []
    def solve():
        nonlocal x
        nonlocal y
        if len(y) < 2:
            for i in range(81):                
                # loop 81 and find first zero cell ... if no zero cells => 
                if x[i] == 0:                 
                    for n in range(1,10):    
                        if possible(x,n,i):   
                            # loop 9 and assign first possible value and save new board to x if no possible => return
                            x[i] = n          
                            solve()           
                            # solve new board if solved (reached last cell)
                            if len(y) > 1:
                                return
                            x[i] = 0          
                            # if stuck at any cell and all 9 values are not possible => ... return inner func and set cell to 0
                    return
            y = y+[x.copy()]   
            # save first two solution if multiple solutions are available or one if only one is available 
    try:
        solve()
        if len(y) == 2:
            # if got 2 solutions mark the  differences between them in the second one
            for i in range(80):
                if y[0][i] != y[1][i]:
                    y[1][i] = [y[0][i],y[1][i]]
        return y
    except:
        return x

if __name__ == "__main__":
    from json1 import board, mat
    a = board()
    s = Fsolve(a)
    mat(a)
    mat(s)











# def xcombine(a):
#     x=[]
#     for i in a:
#         x.extend(i)
#     return x
# def Fsolve(a):
#     xn = 0
#     x = a.copy()
#     def solve():
#         nonlocal x
#         for i in range(81):                # loop 81 and find first zero cell ... if no zero cells => 
#             if x[i] == 0:                 
#                 for n in range(1,10):     
#                     if possible(x,n,i):   # loop 9 and assign first possible value and save new board to x if no possible => return
#                         x[i] = n          
#                         solve()           # solve new board if solved (reached last cell)
#                         x[i] = 0          # if stuck at any cell and all 9 values are not possible => ...
#                 return                    # ... => 
#         nonlocal xn 
#         f = 1/(1-xn)
#         xn = xn + 1
#     try:
#         solve()
#         if 0 in x:
#             print(x)
#             return [x, False]
#         else:
#             return [x, True]
#     except:
#         return [x, False]
