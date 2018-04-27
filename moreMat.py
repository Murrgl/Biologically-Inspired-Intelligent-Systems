# author : Meghana Sathish(mxs7620@rit.edu)

from collections import namedtuple
import numpy as np

Matrix = namedtuple('Matrix', 'rows cols data')
Vector = namedtuple('Vector', 'data')

def subtract(a,b):
    sum = list(map(lambda x, y: x - y, a.data, b.data))
    sm = Matrix(a.rows, a.cols, sum)
    return sm

def makeMatrix(r,c,func):
    num = func()
    mul = r * c
    res = [num] * mul
    temp = Matrix(r,c,res)
    return temp

def setMat(m1,m2):
    temp = m2.data
    for idx in range(0,len(temp)):
        m1.data[idx] = temp[idx]

def colMatrixFromVector(vec):
    r = len(vec.data)
    res = Matrix(r, 1, vec.data)
    return res

def vectorFromColMatrix(mat):
    res = Vector(mat.data)
    return res

def mapMatrix(func,mat):
    temp = []
    for num in mat.data:
        temp.append(func(num))
    res = Matrix(mat.rows, mat.cols, temp)
    return res

def pointProd(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a*b
    elif isinstance(a,float) and isinstance(b,float):
        return a*b
    elif isinstance(a,Vector) and isinstance(b,Vector):
        if len(a.data) != len(b.data):
            raise TypeError
        else:
            res = [x * y for x, y in zip(a.data, b.data)]
            sv = Vector(res)
            return sv
    elif isinstance(a,Matrix) and isinstance(b,Matrix):
        if a.rows != b.rows or a.cols != b.cols :
            raise TypeError
        else:
            res = [x * y for x, y in zip(a.data, b.data)]
            sm = Matrix(a.rows, a.cols, res)
            return sm
    else:
        raise TypeError

def pointProd2(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a*b
    elif isinstance(a,float) and isinstance(b,float):
        return a*b
    elif isinstance(a,Vector) and isinstance(b,Vector):
        res = [x * y for x, y in zip(a.data, b.data)]
        sv = Vector(res)
        return sv
    elif isinstance(a,Matrix) and isinstance(b,Matrix):
        r = min(a.rows, b.rows)
        c = min(a.cols, b.cols)
        res = [x * y for x, y in zip(a.data, b.data)]
        sm = Matrix(r, c, res)
        return sm
    else:
        raise TypeError

def min(a,b):
    if a < b :
        return a
    else:
        return b

def transpose(mat):
    x = split(mat.data, mat.cols)
    data = np.matrix(x)
    trans = np.matrix.transpose(data)
    rev = trans.tolist()
    flat_list = [item for sublist in rev for item in sublist]
    sm = Matrix(mat.cols, mat.rows, flat_list)
    return sm

def split(arr, size):
    '''
    to separate the rows
    :param arr: array to be split
    :param size: number of rows
    :return: lists of lists
    '''
    arrs = []
    while len(arr) > size:
        slice = arr[:size]
        arrs.append(slice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs

def outerProd(mat1, mat2):
    temp = []
    for item in mat1.data:
        for num in mat2.data:
            x = item * num
            temp.append(x)
    sm = Matrix(mat1.rows, mat1.rows, temp)
    return sm

def augmentColMat(mat):
    temp = mat.data
    temp.append(float(1))
    sm = Matrix(mat.rows+1, mat.cols, temp)
    return sm

if (subtract(Matrix(rows=2, cols=3, data=[1, 3, 2, 7, 5, 8]), Matrix(rows=2, cols=3, data=[4, 1, 2, 2, 5, 9])) !=
            Matrix(rows=2, cols=3, data=[-3, 2, 0, 5, 0, -1])):
        print("Error in subtract function")

if ((makeMatrix(3,4,lambda :0.2)) !=
        Matrix(rows=3, cols=4, data=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2])):
    print("Error in make matrix function")

m = Matrix(rows=2, cols=3, data=[1, 3, 2, 7, 5, 8])
mnew = Matrix(rows=2, cols=3, data=[5, 12, 6, 8, 1, -6])
setMat(m, mnew)
if (m != mnew):
    print("Error in SetMat function")

if (colMatrixFromVector(Vector([6,1,9])) != Matrix(rows=3, cols=1, data=[6, 1, 9])):
        print("Error in Column matrix from vector function")

if (vectorFromColMatrix(Matrix(rows=3, cols=1, data=[6, 1, 9])) != Vector(data=[6, 1, 9])):
        print("Vector from column matrix function")

if (mapMatrix(lambda x :x*x, Matrix(rows=2, cols=3, data=[4, 1, 2, 2, 5, 9] )) !=
            Matrix(rows=2, cols=3, data=[16, 1, 4, 4, 25, 81])):
        print("Error in map Matrix function")

if (pointProd(Vector([3,5,7]), Vector([3,5,7])) != Vector(data=[9, 25, 49])):
        print("Error in pointProd function")

if (pointProd2(Matrix(rows=4, cols=1, data=[2,7,-1,8]), Matrix(rows=3, cols=1, data=[-6,7,-1])) !=
            Matrix(rows=3, cols=1, data=[-12, 49, 1])):
        print("Error in pointProd2 function")

if (transpose(Matrix(rows=2, cols=3, data=[4, 1, 5, 9, 5, 10])) != Matrix(rows=3, cols=2, data=[4, 9, 1, 5, 5, 10])):
        print("Error in transponse function")

if (outerProd(Matrix(rows=3, cols=1, data=[6, 1, 9]), Matrix(rows=3, cols=1, data=[5, -3, 12])) !=
            Matrix(rows=3, cols=3, data=[30, -18, 72, 5, -3, 12, 45, -27, 108])):
        print("Error in Outer Prod function")

if(augmentColMat(Matrix(rows=4, cols=1, data=[2,7,-1,8])) != Matrix(rows=5, cols=1, data=[2, 7, -1, 8, 1.0])):
        print("Error in augColMat function")