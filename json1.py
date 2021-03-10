
def board():
    # get json object online with level X: 1|2|3 and return array of 81
    from requests import get
    L = input("Choose level(1|2|3):")
    while L not in ["1","2","3"]:
        L = input("Choose level(1,2,3):")
    r = get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level='+L)
    j = r.json()
    squares = j['squares']
    a = [0 for i in range(81)]
    for i in squares:
        index = i['x']*9 + i['y']
        a[index] = i['value']
    return a

#############################################

def mat(x):
    # print array or arrays of 81 into 9x9 matrix form
    def m(a):
        for i in range(9):
            print(a[i*9:i*9+9])
        print("")
    if type(x[0])==list:
        for i in x:
            m(i)
    else:
        m(x)

############################################

if __name__ == "__main__":
    mat(board())