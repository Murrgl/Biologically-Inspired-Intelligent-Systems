# author : Meghana Sathish(mxs7620@rit.edu)
from collections import namedtuple
import numpy as np

#create a namedtuple Vector

Perceptron = namedtuple('Perceptron','eta weightVec trace')
Vector = namedtuple('Vector','data')
store = []

def makePerceptron(eta, n, func, trace):
    x = makeVector(n+1,func)
    y = Perceptron(eta, x, trace)
    return y

def makeVector(var,func):
    lst = []
    lst.append(func())
    temp = lst * var
    return Vector(temp)

def sigma(x):
    if x>0:
        return 1
    else:
        return 0

def applyPerceptron(p, vec):
    a = p.weightVec.data
    b = vec.data
    prod = np.dot(a,b)
    res = sigma(prod)
    return res

def trainOnce(p, vec, target):
    res = applyPerceptron(p,vec)
    diff = target - res
    if diff==0:
        return False
    else:
        return True

def trainEpoch(p, data):
    temp = create_lst(data)
    orig = np.array(p.weightVec.data)
    x = np.array(p.weightVec.data)
    for idx in range(0,len(temp)):
        bool, diff = trainOnce1(p,temp[idx][0],temp[idx][1])
        vec = np.array(temp[idx][0].data)
        x += p.eta * diff * vec
        for idx in range(0, len(x)):
            p.weightVec.data[idx] = x[idx]
    if orig.tolist() == p.weightVec.data:
        return False
    else:
        return True

def train(p, data, n):
    for idx in range(0,n):
        # print("in")
        bool = trainEpoch(p,data)
        if bool == False:
            break

def trainOnce1(p, vec, target):
        res = applyPerceptron(p, vec)
        diff = target - res
        if diff == 0:
            return False, diff
        else:
            return True, diff

def preprocessData(lst):
    for item in lst:
        ele = loop(item)
        ele.data.append(1)
    return lst

def loop(s):
    for e in s:
        break
    return e

def create_lst(s):
    global store
    for idx in s:
        store.append(idx)
    return store

# p = makePerceptron(.2, 2, lambda: .5, 1)
# if (p !=
#         Perceptron(eta=0.2, weightVec=Vector(data=[0.5, 0.5, 0.5]), trace=1)):
#     print("Error in makePerceptron")
#
# if (sigma(0.5) != 1 or sigma(-1) != 0):
#     print("Error in sigma function")
#
# if (applyPerceptron(p, Vector([0, 1, 1])) != 1):
#     print("Error in apply perceptron")
#
# binary_train_Once_P = trainOnce(p, Vector([0, 1, 1]), 0)
# if (binary_train_Once_P != True):
#     print("Error in Perceptron Train Once")
#
# andset = preprocessData([(Vector([1, 1]), 1), (Vector([1, 0]), 0), (Vector([0, 1]), 0), (Vector([0, 0]), 0)])
#
# if (andset != [(Vector(data=[1, 1, 1]), 1),
#                    (Vector(data=[1, 0, 1]), 0), (Vector(data=[0, 1, 1]), 0), (Vector(data=[0, 0, 1]), 0)]):
#     print("Error in perceprtron preprocess function")
# print(trainEpoch(p,andset))
# print(p)
# train(p,andset,3)
