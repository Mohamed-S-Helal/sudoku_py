from random import sample
from possible import Fsolve
from unify import mod


def randBoard(n):
    z = [0,0,0]
    ra = sample(range(1,10),9)
    rb = sample(range(1,10),9)
    rc = sample(range(1,10),9)
    rr = ra[:3]+2*z+ra[3:6]+2*z+ra[6:]+2*z+\
        z+rb[:3]+2*z+rb[3:6]+2*z+rb[6:]+z+\
        2*z+rc[:3]+2*z+rc[3:6]+2*z+rc[6:]

    a = Fsolve(rr)[0]
    for i in sample(range(81),n):
        a[i] = 0
    
    return a


if __name__ == "__main__":
    from json1 import mat
    mat(randBoard(int(input("number of empty cells:"))))
