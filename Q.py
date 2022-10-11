import numpy as np
import random


# | 5 | 6 |
# | 3 | 4 |
# | 1 | 2 |


matriz_rg = [[0.1, 0.8, 0.1, 0, 0, 0],
            [0, 0.9, 0, 0.1, 0, 0],
            [0.1, 0, 0, 0.8, 0.1, 0],
            [0, 0.1, 0, 0.8, 0, 0.1],
            [0, 0, 0.1, 0, 0.1, 0.8],
            [0, 0, 0, 0, 0, 0]]

matriz_up = [[0.1, 0.1, 0.8, 0, 0, 0],
            [0.1, 0.1, 0, 0.8, 0, 0],
            [0, 0, 0.1, 0.1, 0.8, 0],
            [0, 0, 0.1, 0.1, 0, 0.8],
            [0, 0, 0, 0, 0.9, 0.1],
            [0, 0, 0, 0, 0, 0]]

matriz_lf = [[0.9, 0, 0.1, 0, 0, 0 ],
            [0.8, 0.1, 0, 0.1, 0, 0],
            [0.1, 0, 0.8, 0, 0.1, 0],
            [0, 0.1, 0.8, 0, 0, 0.1],
            [0, 0.9, 0.1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

matriz_down = [[0.9, 0.1, 0, 0, 0, 0],
              [0.1, 0.9, 0, 0, 0, 0],
              [0.8, 0, 0.1, 0.1, 0, 0],
              [0, 0.8, 0.1, 0.1, 0, 0],
              [0, 0, 0.8, 0, 0.1, 0.1],
              [0, 0, 0, 0, 0, 0]]
              
Q_matriz = [[0]*4,[0]*4,[0]*4,[0]*4,[0]*4,[10]*4]

actions_names = ["UP","LF","DW","RG"]

gamma = 1

alpha = 0.5

rewards = [
    #up ,le ,dw ,ri
    [ -1,-10,-10, -1],
    [ -1, -1,-10,-10],
    [ -1,-10, -1, -1],
    [ 10, -1, -1,-10],
    [-10,-10, -1, 10],
    [  0,  0,  0,  0],
]

def bellman(s,a,_s):
    return (rewards[s][a] + (gamma * max(Q_matriz[_s])))


def action_result(sate, transition):
    index = 0
    states = {}
    values = []
    for i in transition:
        if i != 0:
            states[index] = i
            values
    


    

def update_func(s,a,_s):
    Q_matriz[s][a] = Q_matriz[s][a] + alpha*(bellman(s,a,_s) - Q_matriz[s][a])


def call_all():
    state = 0
    while True:
        trial = random.randint(0, 3)
        if trial == 0:
            transition = matriz_up[0]
        
        if trial == 1:
            transition = matriz_lf[0]

        if trial == 2:
            transition = matriz_down[0]

        if trial == 3:
            transition = matriz_rg[0]
            
        next_state = action_result(state,transition)

        print(state,actions_names[trial],next_state)
                
        update_func(state,a,_s)

        state = next_state

        if state == 6:
            break
    
for _ in range(200):
    call_all()


def find_direction(s):
    dir = np.argmax(Q_matriz[s])
    if(dir==0):
        return('UP')
    if(dir==1):
        return('LF')
    if(dir==2):
        return('DW')
    if(dir==3):
        return('RG')

print(find_direction(4) + "|" + "ok")
print(find_direction(2) + "|" + find_direction(3))
print(find_direction(0) + "|" + find_direction(1))
