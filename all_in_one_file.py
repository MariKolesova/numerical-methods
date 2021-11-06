import math


def fx(x):
    return -math.exp(-x) + 2 * x


def fxx(x):
    return -math.exp(-x) + 2


def f(x):
    return math.exp(-x) - 1.9 + math.pow(x, 2)


def cas_parab():
    xn1 = 1.5
    M = fxx(xn1)
    print("M=", M)
    eps = 0.000005
    while True:
        d = (fx(xn1) - math.sqrt(math.pow(fx(xn1), 2) + 2 * M * f(xn1)))/M
        xn1 = xn1 + d
        print("d=", d, "xn1=", xn1)
        if abs(d) <= eps:
            break


def dihotomiya():
    a = 1
    b = 1.5
    eps = 0.000005
    num = 0
    while True:
        num += 1
        c = (a + b) / 2
        fc = f(c)
        if (b - a) / 2 < eps:
            break
        if f(a) * f(c) < 0:
            print("a=", a, " бывшее b=", b, "c=, которое будет b", c, 'f(c)=', fc, "num=", num)
            b = c
        else:
            print("бывшее a=,", a, "b=", b, "c=, которое будет a", c, 'f(c)=', fc, "num=", num)
            a = c


def podvizh_hordy():
    xn0 = 1
    xn1 = 1.5
    eps = 0.000005
    shag = -1
    while True:
        shag += 1
        d = f(xn1) * (xn1 - xn0) / (f(xn1) - f(xn0))
        xn2 = xn1 - d
        print("shag ", shag, "xn0=", xn0, "xn1=", xn1, "fph(xn0)=", f(xn0), "fph(xn1)=", f(xn1), "d=", d, "xn2=", xn2, "f(xn2)=", f(xn2))
        if abs(d) < eps:
            break
        xn0 = xn1
        xn1 = xn2


def newton():
    xk = 1.5
    shag = 0
    while True:
        xk_1 = xk - f(xk) / fx(1.5)
        shag += 1
        print("shag=", shag, "xk=", xk, "xk_1", xk_1)
        if abs(xk_1 - xk) < 0.000005:
            break
        xk = xk_1


def nepodvizh_hordy():
    a = 1
    b = 1.5
    eps = 0.000005
    shag = 1
    c = a - (f(a) / (f(b) - f(a))) * (b - a)
    c_shag = a - (f(a) / (f(b) - f(a))) * (b - a)
    while True:
        shag += 1
        if f(a) * f(c_shag) < 0:
            # c = a - (f(a) / (f(b) - f(a))) * (b - a)
            b = c_shag
        elif f(b) * f(c_shag) < 0:
            # c = a - (f(a) / (f(b) - f(a))) * (b - a)
            a = c_shag
        c = c_shag
        c_shag = a - (f(a) / (f(b) - f(a))) * (b - a)
        if abs(c_shag - c) < eps:
            break
        print("shag:", shag, "a:", a, "ck:", c, "b:", b, "ck_1:", c_shag, )


def phi(x):
    return math.sqrt(1.9 - math.exp(-x))


def simple_iteration():
    a = 1
    b = 1.5
    eps = 0.000005
    shag = 1
    x_old = 1.25
    while True:
        shag += 1
        x_new = phi(x_old)
        print("shag:", shag, "x_old:", x_old, "x_new:", x_new)
        if abs(x_new - x_old) < eps:
            break
        x_old = x_new



def main():
    simple_iteration()


if __name__ == '__main__':
    main()
