# author : Meghana Sathish(mxs7620@rit.edu)
from collections import namedtuple

#create a namedtuple Vector

Vector = namedtuple('Vector',['data'])

def makeVector(var,func):
    lst = []
    lst.append(func())
    temp = lst * var
    return Vector(temp)

def setVec(v1,v2):
    temp = v2.data
    for idx in range(0,len(temp)):
        v1.data[idx] = temp[idx]

# v1 = makeVector(3, lambda : .5)
# v2 = Vector([98, 99, 100])
# setVec(v1,v2)
# print(v1)

# if ((makeVector(3, lambda: .5)) != Vector(data=[0.5, 0.5, 0.5])):
#     print("Error in makeVector function")
# try:
#     v1 = makeVector(3, lambda : .5)
#     v2 = Vector([98, 99, 100])
#     setVec(v1,v2)
#     if v1 != v2:
#         print("Error in setVec function")
# except:
#     print("Error in setVec function")
