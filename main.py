from scipy.integrate import quad
import math


def f(x):
    return round(math.exp(pow(x, 3)), 10)


def f_xx(x):  # вторая производная
    return 9 * pow(x, 4) * round(math.exp(pow(x, 3)), 10) + 6 * x * round(math.exp(pow(x, 3)), 10)


def method_srednih_pryamougolnicov():
    itog_sum = 0
    kv_s = 0
    for i in range(10):
        l = f(i * 0.1 + 0.05)
        print('xi плюс аш пополам ниже')
        print(i * 0.025 + 0.0125)  # print(xi)
        print("значения 4 строки таблицы ниже")
        print(l)  # значения 4 строки таблицы
        kv_s += l
        itog_sum += l
        print(itog_sum)
    print("сумма значений ф-й от промежуточной точки")
    print(kv_s)
    print('сумма значений умножить на h')
    print(0.025 * kv_s)
    print(l)
    print(1.34190441797742 - 0.1 * itog_sum)  # абсолютная погрешность
    print("вторая производная")
    sum_sum = 0
    for i in range(41):
        x = i * 0.025
        kvadr_sum = 9 * pow(x, 4) * round(math.exp(pow(x, 3)), 10) + 6 * x * round(math.exp(pow(x, 3)), 10)
        sum_sum += kvadr_sum
        print(kvadr_sum)
    print(sum_sum)
    print(sum_sum * 0.001 / 24)  # оценка погрешности


def method_trapexiy():
    sum_function = 0
    for i in range(21):
        print(i, f(i * 0.05))  # функции от икс итое, 3 строка
    sum_two_elements = 0
    for i in range(21):
        if i == 0 or i == 20:
            sum_two_elements += f(i * 0.05)
        else:
            sum_function += f(i * 0.05)
    print("сумма 1 по 39 слагаемые")
    print(sum_function)
    print('сумма из 0 и 40 слагаемых')
    print(sum_two_elements)  # дробь из 0 и 9 слагаемых
    print('дробь из 0 и 40 слагаемых')
    print(sum_two_elements / 2)
    print('общая сумма')
    print(sum_function + sum_two_elements / 2)
    print('аш на сумму')
    print(0.05 * (sum_function + sum_two_elements / 2))
    print('абсолютная погрешность')
    print(1.34190441797742 - (0.05 * (sum_function + sum_two_elements / 2)))

    # считаем вторые производные от икс итое
    sum_f_xx = 0
    for i in range(20):
        x = i * 0.05
        sum_f_xx += f_xx(x)
        print(f_xx(x))
    print('сумма вторых производных')
    print(sum_f_xx)
    print('погрешность')
    print(sum_f_xx * 0.01 / 12)
    print('квадратурная сумма')
    print((f(0) + f(1)) / 2)




if __name__ == '__main__':
    method_trapexiy()
