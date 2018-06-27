import numpy as np

x = np.array([1,2,4,5,6,7,8,12,30])
y = np.array([1,2,4,5,6,7,8,12,30])

w = np.array([[1,4],[5,13]])
z = np.array([[0,1],[10,10]])

# 1
print(x)

# 2
print(x[x>=8])

# 3
print(x[x%2 == 0])

# 4
print(x + y)

# 5
print(w + z)

# 6
print(w * 10)

# 7 
print(w[0][1])
