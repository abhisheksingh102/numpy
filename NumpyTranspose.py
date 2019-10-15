import numpy as np

n,m=map(int,input().split())
A=[]
for i in range(n):
    A.append(list(map(int,input().split())))
A=np.array(A)
print(A.T)
print(A.flatten())