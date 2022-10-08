import numpy as np
Q = [[0]*4,[0]*4,[0]*4,[0]*4,[0]*4,[10]*4]
alpha = 0.5
# | 5 | 6 |
# | 3 | 4 |
# | 1 | 2 |
r = [
    #up ,le ,dw ,ri
    [ -1,-10,-10, -1],
    [ -1, -1,-10,-10],
    [ -1,-10, -1, -1],
    [ 10, -1, -1,-10],
    [-10,-10, -1, 10],
    [  0,  0,  0,  0],
]
walls = [
    []
]
def if_here_and_do_this_where_I_go(s,a):
    return 
def bellman(s,a,_s):
    return (r[s][a] + max(Q[_s]))

def update_func(s,a,_s):
    Q[s][a] = Q[s][a] + alpha*(bellman(s,a,_s) - Q[s][a])

def call_all():
    for s in range(5):
        for a in range(4):
            if(r[s][a] == -10):#bateu na parede
                update_func(s,a,s)
            elif(a==0):
                update_func(s,a,s+2)
            elif(a==1):
                update_func(s,a,s-1)
            elif(a==2):
                update_func(s,a,s-2)
            elif(a==3):
                update_func(s,a,s+1)

for _ in range(100):
    call_all()

def find_direction(s):
    dir = np.argmax(Q[s])
    if(dir==0):
        return('up')
    if(dir==1):
        return('lf')
    if(dir==2):
        return('dw')
    if(dir==3):
        return('rg')

print(find_direction(4) + "|" + "ok")
print(find_direction(2) + "|" + find_direction(3))
print(find_direction(0) + "|" + find_direction(1))
