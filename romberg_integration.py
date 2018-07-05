import time
import numpy as np


def func(x):
    # return 0.3+20*x-140*pow(x,2)+730*pow(x,3)-810*pow(x,4)+200*pow(x,5)
    return 0.2+25*x-200*pow(x,2)+675*pow(x,3)-900*pow(x,4)+400*pow(x,5)


def do_summation(n, a, h):
    _sum = 0
    for i in range(1,n):
        _sum = _sum + func(a+i*h)
    return _sum


def trapezoid(n, a, b):
    h = (b - a) / n
    return 0.5*h*(func(a) + func(b) + 2*do_summation(n, a, h))


def romberg(a, b, order):
    M = np.zeros((order,order),float)  # create an array of zeroes of order*order

    for i in range(0,order):
        n = 2**i
        M[i,0] = trapezoid(n, a, b)
        for k in range(0,i):
            n = k + 2
            M[i, k+1] = 1.0/(4**(n-1)-1)*(4**(n-1)*M[i, k] - M[i-1, k])  # Romberg untegration formula

    return M[i, k+1]


def main():
    a = 0.2;b = 0.8
    start = time.time()
    print(romberg(a, b, 3))
    end = time.time()
    time_elapsed = end - start
    print('Time Elapsed:' + str(time_elapsed) + ' Seconds')

    # Expected output: 1.4172
    # Result of this program: 1.4172
    # Time elapsed for six executions:
    # 0.00009059906005859375,0.00009512901306152344,0.00008726119995117188,0.00009918212890625,0.00009965896606445312,0.00008797645568847656
    # Average time elapsed:0.00009330113

if __name__ == '__main__':
    main()
