#name-jayvee shah
#prn-25070123058
#a3

#tools for eda- study of numpy library
#declaration of numpy
import numpy as np

a=np.array([1,2,3,4,5])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(b)
print(a.ndim)
print(b.ndim)
print(a.shape)
print(b.shape)
print(a.dtype)
print(b.dtype)

#inbuilt functions using numpy
print(np.zeros((4,3)))
print(np.ones((2,4)))
print(np.eye(3))
print(np.arange(1,10,2))
print(np.linspace(0,1,5))

print(b*2)
print(a+5)

print(np.mean(a))
print(np.median(a))

print(np.min(a))
print(np.max(a))
print(np.sum(a))
