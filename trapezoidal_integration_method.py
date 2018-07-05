import time


def func(x):
    # return 0.3+20*x-140*pow(x,2)+730*pow(x,3)-810*pow(x,4)+200*pow(x,5)
    return 0.2+25*x-200*pow(x,2)+675*pow(x,3)-900*pow(x,4)+400*pow(x,5)


def do_summation(n,a,h):
    _sum = 0
    for i in range(1,n):
        _sum = _sum + func(a+i*h)
    return _sum


def trapezoid(n,a,b):
    h = (b - a) / n
    return 0.5*h*(func(a) + func(b) + 2*do_summation(n, a, h))


def main():
    a = 0.2
    b = 0.8
    n = 6
    start= time.time()
    result = trapezoid(n, a, b)
    print(result)
    end=time.time()
    time_elapsed= end-start
    print('Time Elapsed:' + str(time_elapsed)+' Seconds')
    # Expected output: 1.4172
    # Result of this program: 1.397500000000007
    # Time elapsed for six executions:
    # 0.00013566017150878906,0.000141143798828125,0.00012421607971191406,0.00008678436279296875,0.00008702278137207031,0.00008726119995117188
    # Average time elapsed:0.00011034806

if __name__ == '__main__':
    main()

