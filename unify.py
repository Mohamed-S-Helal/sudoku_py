from possible import Fsolve
from json1 import board, mat
from random import shuffle

def mod(x):
    x2 = x.copy()
    a = Fsolve(x2)
    if len(a) == 1:
        return x2,a[0]
    else:
        ii = a[1].copy()
        shuffle(ii)
        for i in ii:
            if type(i) == list:
                # print(i)
                # print(a[1].index(i))
                # x1[a[1].index(i)] = i[0]
                x2[a[1].index(i)] = i[0]
                break
        # c+=1
        # print(c)
        return mod(x2)

############################################

if __name__ == "__main__":
    x = board()
    s = mod(x)
    print(s[0].count(0))
    mat(x)
    mat(s)
