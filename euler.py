# author : Meghana Sathish (mxs7620@rit.edu)


def euler(h,tb,A,x0,F):
    '''
    Euler function to solve differential equations.
    function that accepts x0 and F as lists
    :param h:
    :param tb:
    :param A:
    :param x0:
    :param F:
    :return:
    '''
    for di, da in zip(x0, F):
        t = 0
        x = di
        while t <= tb:
            A(t, [x])
            x += h * da([x], t)
            t += h

T = []
X = []

def update(t, x):
  global T, X
  T.append(t)
  X.append(x)

def check_for_euler():
    T.clear()
    X.clear()
    euler(0.025, .1, update, [1], [(lambda x, t: x[0])])

    if (T != [0, 0.025, 0.05, 0.07500000000000001, 0.1]):
        print("Error in Euler T list")
    if (X != [[1], [1.025], [1.050625], [1.0768906249999999], [1.103812890625]]):
        print('Error in Euler X list')