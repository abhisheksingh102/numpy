import numpy as np
n,m=map(int,input().split())
s=np.identity(n,dtype=int)
# or s=np.eye(n,m,dtype=int)
print(s)