"""dz9_2"""


def find_max_1(f, points):
    """
    (function, list(number)) -> (number)

    Find and return maximal value of function f in points.

    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    return f(max(points, key=f))


def find_max_2(f, points):
    """
    (function, list(number)) -> (number)

    Find and return list of points where function f has the maximal value.

    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """
    return [i for i in points if f(i) == f(max(points, key=f))]


def compute_limit(seq):
    """
    (function) -> (number)

    Compute and return limit of a convergent sequence.

    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    """
    lst = []  # the list sequence elements

    i = 0

    while True:
        n = 10 ** i  # the number of element
        lst.append(seq(n))  # adding new element

        # check the difference between elements
        if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:
            return round(lst[i], 1)
        i += 1


# print(compute_limit(lambda n: (n ** 2 + n) / n ** 2))


def compute_derivative(f, x_0):
    """
    (function, number) -> (number)

    Compute and return derivative of function f in the point x_0.

    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    aprox = []
    i = 0
    while True:
        dx = 10 ** -i
        x = x_0 + dx
        dF = f(x)
        x = x_0
        dF -= f(x)
        der = dF / dx
        aprox.append(der)
        if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
            return round(aprox[i], 1)
        i += 1


# compute_derivative(lambda x: x ** 2 + x,2)


def get_tangent(f, x_0):
    """
    (function, number) -> (str)

    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    f_xo = f(x_0)
    der_f_xo = compute_derivative(f, x_0)
    first_additive = f'{round(der_f_xo, 1)} * x '
    second_additive = f'{round(f_xo + der_f_xo * -x_0, 1)}'
    if first_additive[0] == '-':
        first_additive = f'- {-1 * round(der_f_xo, 1)} * x '
    if second_additive[0] == '-':
        second_additive = f'- {-round(f_xo + der_f_xo * -x_0, 1)}'
    else:
        second_additive = f'+ {round(f_xo + der_f_xo * -x_0, 1)}'

    return first_additive + second_additive


def get_root(f, a, b):
    """
    (function, number, number) -> (number)

    Compute and return root of the function f in the interval (a, b).

    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    while abs(b - a) > 0.0001:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return round((a + b) / 2, 1)
