#!/usr/bin/python3

# 2 - 2 - Perceptron Learning Algorithm
import numpy as np

# Augmented vector
W1=[[0,0,0,1],
    [1,0,0,1],
    [1,0,1,1],
    [1,1,0,1]]

# * (-1)
W2=[[0,0,-1,-1],
    [0,-1,-1,-1],
    [0,-1,0,-1],
    [-1,-1,-1,-1]]

w=[-1,-2,-2,0]
print(len(W2))
tempW12=W1+W2
nextw=w
wNum=1
convergence=0
iteration=0
while not convergence:
    convergence=1
    iteration+=1
    print("while num is "+str(iteration))
    for index in range(len(tempW12)):
        a = nextw
        b = tempW12[index]
        matrixResult=np.matmul(a,b)
        print(f'W^T({wNum})X_{index+1}={a}*{b}T={matrixResult}')

        wNum+=1
        if matrixResult>0:
            nextw=a
            print(f'W({wNum})=W({wNum-1})={nextw}')
        else:
            convergence=0
            nextw=[i+j for i,j in zip(a,b)]
            print(f'W({wNum})=W({wNum-1})+X{wNum-1}={nextw}')
