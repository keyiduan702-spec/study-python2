import numpy as np

#@运算符
#相乘条件：左列数=右行数
#相乘结果：左行数*右列数
A=np.array([[1,2,3],
            [3,4,5]])#2*3
B=np.array([[5,6],
            [7,8],
            [8,9]])#3*2
print(A@B)
#np.dot()函数
C=np.dot(A,B)
print(C)