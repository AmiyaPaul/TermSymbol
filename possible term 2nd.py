from itertools import combinations
from itertools import permutations
import numpy as np

print("Welcome ! \nCalculate the probable Term Symbol")
orbit = input("Write the orbital like - 3s1 \n")

def listmaking(orbit):
    def orbitalanal(orbital):
        a = orbital[0]
        b = orbital[1]
        c = orbital[2:]

        return [a, b, c]

    lset = {'s': 1, 'p': 3, 'd': 5, 'f': 7, 'g': 9}

    tupi = orbitalanal(orbit)
    bat = int(tupi[2])
    cat = lset[tupi[1]] * 2
    lit = []

    for i in range(bat):
        lit.append(1)
    for j in range(cat-bat):
        lit.append(0)

    return lit

lit = listmaking(orbit)

a = []
b = []
term = []

for k in permutations(lit):
    a.append(k)

for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])

b = np.array(b)
st = {0: "S", 1: "P", 2: "D", 3: "F", 4: "G", 5: "H", 6: "I"}
for sub in b:
    S = 0
    L = 0
    for s in range(len(sub)):
        if (s + 1) % 2 != 0:
            S += 0.5 * sub[s]
        elif (s + 1) % 2 == 0:
            S += -0.5 * sub[s]

        case = len(lit) / 2

        if case == 1:
            if s <= 1:
                L += 0 * sub[s]
        elif case == 3:
            if s <= 1:
                L += 1 * sub[s]
            elif s <= 3:
                L += 0 * sub[s]
            else:
                L += -1 * sub[s]

        elif case == 5:
            if s <= 1:
                L += 2 * sub[s]
            elif s <= 3:
                L += 1 * sub[s]
            elif s <= 5:
                L += 0 * sub[s]
            elif s <= 7:
                L += -1 * sub[s]
            else:
                L += -2 * sub[s]

    sm = 2 * abs(S) + 1
    ang = st[abs(L)]

    h = (sm, ang)
    if h not in term:
        term.append(h)

print("The energy order is higher to lower : \n")

s1 = []
s2 = []
ts = {"S": 0, "P": 1, "D": 2, "F": 3, "G": 4, "H": 5, "I": 6}
for val in term:
    if val[0] not in s1:
        s1.append(val[0])

for i in s1:
    sk = []
    for val in term:
        if i == val[0]:
            sk.append(ts[val[1]])
    sk.sort()
    s2.append(sk)

for i in range(len(s1)):
    for j in range(len(s2[i])):
        kk = f"{s1[i]} {st[s2[i][j]]}"
        print(kk)