import sqlite3
from unify import mod
from json1 import mat
from generate import randBoard

def fill():
    n = input("Number of puzzels:")
    while not n.isdecimal():
        n = input("Number of puzzels:")
    n = int(n)

    m = input("number of empty cells:")
    while not m.isdecimal():
        m = input("Number of puzzels:")
    m = int(m)

    i = 1
    while i <= n:
        print("---------------")
        print(i) 
        db = sqlite3.connect("sudoku.db")
        db.execute("create table if not exists mytable (id integer primary key, board text, solved text)")
        a = mod(randBoard(m))
        
        x = ','.join(map(str, a[0]))
        y = ','.join(map(str, a[1]))
        db.cursor().execute("insert into mytable (board, solved) values (?, ?)", (x, y))
        db.commit()
        mat(a)
        i+=1

if __name__ == "__main__":
    fill()
