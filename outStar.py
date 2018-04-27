# author : Meghana Sathish (mxs7620@rit.edu)

import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def e1(h,tb,val,x0,i,F):
    '''
    function that accepts x0 and F as lists
    :param h:
    :param tb:
    :param A:
    :param x0:
    :param F:
    :return:
    '''
    for dx, di, da in zip(x0, i, [F[0]]):
        t = 0
        x = dx
        i = di
        count = 0
        while t <= tb:
            # i = temp(count)
            # print(i)
            x += h * da([x], t, i)
            # A(t, [x])
            t += h
            count+=1
            return x


def e2(h,tb,x0,x,w,i,F):
    for dx, da in zip(x, F):
        t = 0
        x = dx
        count = 0
        while t <= tb:
            # i = temp(count)
            x += h * da(x, t, x0, w, i)
            t += h
            count+=1
            return x

def e3(h,tb,x0,x,w,F):
    for dx, dw, da in zip(x, w, F):
        t = 0
        x = dx
        w = dw
        count = 0
        while t <= tb:
            # i = temp(count)
            x += h * da(x, t, x0, w)
            t += h
            count+=1
            return x

def temp(count):
    if count % 10 == 0:
        i = [2]
    elif (count-1)%10 == 0:
        i = [2]
    else:
        i = [0]
    return i

def star(h,tb,val,xval,F):
    x1 = val[0]
    x2 = val[1]
    x3 = val[2]
    x4 = val[3]
    w1 = val[4]
    w2 = val[5]
    w3 = val[6]
    w4 = val[7]
    o1 = 0.4
    o2 = 0.3
    o3 = 0.2
    o4 = 0.1
    temp3 = []
    temp3.append(o1)
    temp3.append(o2)
    temp3.append(o3)
    temp3.append(o4)
    O.append(temp3)
    x0 = xval[0]
    step = 0
    fig = plt.figure()
    t =0
    while step<=10000:
        print("step",step)
        while t<=tb:
            i = temp(step)
            x0 = e1(h,tb,val,[x0],i,F)
            if (step-2)%10==0 or (step-3)%10==0:
                i[0]=2
            else:
                i[0]=0
            i1 = i[0] * o1
            x1 = e2(h,tb,x0,[x1],w1,i1,[F[1]])
            i2 = i[0] * o2
            x2 = e2(h, tb, x0, [x2], w2, i2, [F[1]])
            i3 = i[0] * o3
            x3 = e2(h, tb, x0, [x3], w3, i3, [F[1]])
            i4 = i[0] * o4
            x4 = e2(h, tb, x0, [x4], w4, i4, [F[1]])
            w1 = e3(h,tb,x0,[x1],[w1],[F[2]])
            w2 = e3(h, tb, x0, [x2], [w2], [F[2]])
            w3 = e3(h, tb, x0, [x3], [w3], [F[2]])
            w4 = e3(h, tb, x0, [x4], [w4], [F[2]])
            x = x1 + x2 + x3 + x4
            w = w1 + w2 + w3 + w4
            xx1 = x1/x
            xx2 = x2/x
            xx3 = x3/x
            xx4 = x4/x
            ww1 = w1/w
            ww2 = w2/w
            ww3 = w3/w
            ww4 = w4/w
            global W, X
            temp1 = []
            temp2 = []
            if step%100 == 0:
                O.append(temp3)
                temp1.append(ww1)
                temp1.append(ww2)
                temp1.append(ww3)
                temp1.append(ww4)
                temp2.append(xx1)
                temp2.append(xx2)
                temp2.append(xx3)
                temp2.append(xx4)
                print(temp1)
                print(temp2)
                X.append(temp1)
                W.append(temp2)
            t += h
        step += 1
    plt.plot(X)
    plt.plot(W)
    plt.plot(O)
    plt.show()
    print(X)
    print(W)
    print(O)
    fig.savefig("1final.pdf", bbox_inches='tight')

def star1(h,tb,val,xval,F):
    x1 = val[0]
    x2 = val[1]
    x3 = val[2]
    x4 = val[3]
    w1 = val[4]
    w2 = val[5]
    w3 = val[6]
    w4 = val[7]
    o1 = 0.4
    o2 = 0.3
    o3 = 0.2
    o4 = 0.1
    temp3 = []
    temp3.append(o1)
    temp3.append(o2)
    temp3.append(o3)
    temp3.append(o4)
    O.append(temp3)
    x0 = xval[0]
    step = 0
    fig = plt.figure()
    flag = False
    while step<=10000:
        print("step",step)
        i = temp(step)
        x0 = e1(h,tb,val,[x0],i,F)
        if (step - 2) % 10 == 0:
            if flag==False:
                i1 = 0.8
                i2 = 0.6
                i3 = 0.4
                i4 = 0.2
                flag = True
            else:
                i1 = 0.5
                i2 = 0.5
                i3 = 0.3
                i4 = 0.7
                flag = False
        else:
            if (step-2)%10 == 0 or (step-3)%10 == 0:
                i[0] = 2
            else:
                i[0] = 0
            i1 = i[0] * o1
            i2 = i[0] * o2
            i3 = i[0] * o3
            i4 = i[0] * o4
        x1 = e2(h, tb, x0, [x1], w1, i1, [F[1]])
        x2 = e2(h, tb, x0, [x2], w2, i2, [F[1]])
        x3 = e2(h, tb, x0, [x3], w3, i3, [F[1]])
        x4 = e2(h, tb, x0, [x4], w4, i4, [F[1]])
        w1 = e3(h,tb,x0,[x1],[w1],[F[2]])
        w2 = e3(h, tb, x0, [x2], [w2], [F[2]])
        w3 = e3(h, tb, x0, [x3], [w3], [F[2]])
        w4 = e3(h, tb, x0, [x4], [w4], [F[2]])
        x = x1 + x2 + x3 + x4
        w = w1 + w2 + w3 + w4
        xx1 = x1/x
        xx2 = x2/x
        xx3 = x3/x
        xx4 = x4/x
        ww1 = w1/w
        ww2 = w2/w
        ww3 = w3/w
        ww4 = w4/w
        global W, X
        temp1 = []
        temp2 = []
        if step%100 == 0:
            O.append(temp3)
            temp1.append(ww1)
            temp1.append(ww2)
            temp1.append(ww3)
            temp1.append(ww4)
            temp2.append(xx1)
            temp2.append(xx2)
            temp2.append(xx3)
            temp2.append(xx4)
            print(temp1)
            print(temp2)
            X.append(temp1)
            W.append(temp2)
        step += 1
    plt.plot(X)
    plt.plot(W)
    plt.plot(O)
    plt.show()
    print(X)
    print(W)
    print(O)
    fig.savefig("2final.pdf", bbox_inches='tight')

W = []
X = []
O =[]

def check():
    star(0.01, 1, [0.37,0.33,0.17,0.27,0.21,0.31,0.11,0.22],[0],[(lambda x, t, i: -5*x[0]+i),(lambda x, t, x0, w, i: (-5*x) + (x0*w) + i),(lambda x, t, x0, w: x0*(((-0.1)*w)+x))])
    star1(0.01, 10, [0.37,0.33,0.17,0.27,0.21,0.31,0.11,0.22],[0],[(lambda x, t, i: -5*x[0]+i),(lambda x, t, x0, w, i: (-5*x) + (x0*w) + i),(lambda x, t, x0, w: x0*(((-0.1)*w)+x))])


check()

