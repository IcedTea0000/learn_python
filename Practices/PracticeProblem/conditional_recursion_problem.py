import time
import datetime


def convert_time1():
    """convert Epoch time to date time"""
    epoch_time = time.time()
    datetime_time = datetime.datetime.fromtimestamp(epoch_time)
    return datetime_time


def check_fermat(a, b, c, n):
    """4 integer is Fermat Theorem if
    an + bn = cn
    """
    return (a ** n + b ** n) == c ** n


def input_check_fermat():
    """input 4 positive integer from keyboard and check fermat"""
    a = int(input('Input a: '))
    b = int(input('Input b: '))
    c = int(input('Input c: '))
    n = int(input('Input n: '))
    if check_fermat(a, b, c, n):
        print('Good fermat')
    else:
        print('Bad fermat')


def ack(m, n):
    """Computes the Ackermann function A(m, n)
    See http://en.wikipedia.org/wiki/Ackermann_function
    n, m: non-negative integers
    """
    if (m < 0) or (n < 0):
        print('Error, must input positive integer')
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


if __name__ == '__main__':
    print(convert_time1())
    input_check_fermat()
    print(ack(3, 4))
