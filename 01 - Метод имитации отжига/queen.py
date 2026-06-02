
import numpy as np

import matplotlib.pyplot as pt

N = 20

Pos = []

for n in range(N):
    Pos.append(n)


def H(Pos):
    res = 0
        
    for n in range(N):
        k = n - 1
        while k >= 0:
            if Pos[k] == (Pos[n] + (n - k)):
                res = res + 1

            if Pos[k] == (Pos[n] - (n - k)):
                res = res + 1
            k = k - 1

        k = n + 1
        while k < N:
            if Pos[k] == (Pos[n] + (k - n)):
                res = res + 1

            if Pos[k] == (Pos[n] - (k - n)):
                res = res + 1
            k = k + 1
                
    return res

def G(Pos):
    i = 0
    j = 0
    while i == j:
        i = np.random.randint(0, N)
        j = np.random.randint(0, N)
            
    a = Pos[i]
    Pos[i] = Pos[j]
    Pos[j] = a
    
    return Pos


T0 = 100

alpha = 0.98

k = 0

T = T0

L = 200

t = []
x = []
Hx = []
TA = []
E = []
D = []

s = Pos

L = 10000

for i in range(L):

    if H(s) == 0:
        print("H(s) == 0")
        break

    Hs = H(s)
    s_ = G(s.copy())
    Hs_ = H(s_)
    Delta = Hs_ - Hs
    D.append(Delta)

    if Delta < 0:
        s = s_
        e = 0
        print("s = {0}".format(s))
    else:
        r = np.random.uniform(0, 1)
        e = np.exp(-Delta / T)
        if r < e:
            print("s = {0} rnd".format(s))
            s = s_

    print("Hs = {0}, Hs_ = {1}, Delta = {2}, T = {5}, e = {6}".format(Hs, Hs_, Delta, s, s_, T, e))
    
    T = alpha * T
    TA.append(T)
    t.append(i)
    Hx.append(Hs)
    E.append(e)

print("Найденный вариант = {0}; значение = {1}".format(s, H(s)))

# график количества ферзей под боем
pt.plot(t, Hx)
pt.grid(True)
pt.show()

# график температуры
pt.plot(t, TA)
pt.grid(True)
pt.show()

# график Delta на каждой итерации
pt.plot(t, D)
pt.grid(True)
pt.show()

# график e - порога случайной величины из условия присваивания значения s
pt.plot(t, E)
pt.grid(True)
pt.show()