# author : Meghana Sathish(mxs7620@rit.edu)

from collections import namedtuple

#function to create a namedtuple Vector
def Vector(data):
    '''

    :param data: a list of integers
    :return: vector
    '''
    Vector = namedtuple('Vector','data')
    return Vector

# function to create a namedtuple Matrix
def Matrix(rows,cols,data):
    '''

    :param rows: number of rows in matrix
    :param cols: number of cols in matrix
    :param data: list of the integers
    :return: matrix
    '''
    Matrix = namedtuple('Matrix', 'rows cols data')
    return Matrix

def add(a,b):
    '''
    function to add arguments passed
    :param a: first argument
    :param b: second argument
    :return: the resulting sum of same type as argument
    '''
    if isinstance(a,int) and isinstance(b,int):
        return a+b
    elif isinstance(a,float) and isinstance(b,float):
        return a+b
    elif isinstance(a,Vector) and isinstance(b,Vector):
        sum = map(lambda x,y : x+y , a.data,b.data)
        sv = Vector(sum)
        return sv
    elif isinstance(a,Matrix) and isinstance(b,Matrix):
        sum = map(lambda x, y: x + y, a.data, b.data)
        sm = Matrix(a.rows,a.cols,sum)
        return sm
    else:
        raise TypeError

def scale(a,b):
    '''
    scaling
    :param a: first argument
    :param b: second argument
    :return: object of same type as arguments
    '''
    if isinstance(a,int) and isinstance(b,int):
        return a*b
    elif isinstance(a,int) and isinstance(b,float):
        return a*b
    elif isinstance(a,int) and isinstance(b,Vector):
        res = map( lambda x : x*a , b.data)
        sv = Vector(res)
        return sv
    elif isinstance(a,int) and isinstance(b,Matrix):
        res = map(lambda x: x * a, b.data)
        sm = Matrix(b.rows, b.cols, res)
        return sm

def dot(a,b):
    '''
    scalar result of dot product of the arguments
    :param a: integer
    :param b: any object
    :return: object of same type as b
    '''
    x=len(a.data)
    y=len(b.data)
    if x==y:
        return sum([a.data[i]*b.data[i] for i in range(len(a.data))])
    else:
        raise TypeError

def mult(a, b):
    '''
    compute matrix product
    :param a: first matrix
    :param b: second matrix
    :return: resulting matrix
    '''
    if a.cols == b.rows:
        x = split(a.data, a.cols)
        y = split(b.data, b.cols)
        res = []
        for i in range(0, len(x)):
            store = []
            for j in range(0, len(y[0])):
                mul = 0
                for k in range(0, len(x[0])):
                    mul += x[i][k] * y[k][j]
                store.append(mul)
            res.append(store)
        flat_list = [item for sublist in res for item in sublist]
        v = Matrix(a.rows, b.cols, flat_list)
        return v
    else:
        raise TypeError


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
