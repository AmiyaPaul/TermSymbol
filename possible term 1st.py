import numpy as np

def orbitalanal(orbital):
    a = orbital[0]
    b = orbital[1]
    c = orbital[2:]

    return [a, b, c]


orbital = "2p2"

tupi = orbitalanal(orbital)

lset = {'s': 0, 'p': 1, 'd': 2, 'f': 3, 'g': 4, 'h': 5, 'i':6, 'k':7}

e = int(tupi[2])
l_max = lset[tupi[1]]

S_max = e * 0.5
L_max = e * l_max

if e == 1:
    S = tuple([S_max])
elif e % 2 == 0:
    S = np.arange(S_max, -1, -1)
elif e % 2 != 0:
    S = np.arange(S_max, 0, -1)

L = np.arange(L_max, -1, -1)

print(L, S)

def term(c):
    if c == 0:
        k = "S"
    elif c == 1:
        k = "P"
    elif c == 2:
        k = "D"
    elif c == 3:
        k = "F"
    elif c == 4:
        k = "G"
    elif c == 5:
        k = "H"
    elif c == 6:
        k = "I"
    elif c == 7:
        k = "K"
    elif c == 8:
        k = "L"
    elif c == 9:
        k = "M"
    elif c == 10:
        k = "N"
    elif c == 11:
        k = "O"
    elif c == 12:
        k = "Q"
    else:
        k = None
    return k



for i in S:
    for j in L:
        SM = int(2*i + 1)
        if SM >= 3:
            if j != L_max:
                trms = []
                ang = term(j)
                trm = f"{SM} {ang}"
                trms.append(trm)
                print(trms)
        else:
            trms = []
            ang = term(j)
            trm = f"{SM} {ang}"
            trms.append(trm)
            print(trms)





