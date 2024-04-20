from functools import lru_cache

def find_max_1(f, points):
    @lru_cache(maxsize=None)
    def f_cached(x):
        return f(x)
    return f_cached(max(points, key=f_cached))

def find_max_2(f, points):
    @lru_cache(maxsize=None)
    def f_cached(x):
        return f(x)
    max_value = f_cached(max(points, key=f_cached))
    return (i for i in points if f_cached(i) == max_value)

def compute_limit(seq):
    lst = []
    i = 0
    while True:
        n = 10 ** i
        lst.append(seq(n))
        if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:
            return round(lst[i], 1)
        i += 1

def compute_derivative(f, x_0):
    @lru_cache(maxsize=None)
    def f_cached(x):
        return f(x)
    aprox = []
    i = 0
    while True:
        dx = 10 ** -i
        x = x_0 + dx
        dF = f_cached(x)
        x = x_0
        dF -= f_cached(x)
        der = dF / dx
        aprox.append(der)
        if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
            return round(aprox[i], 1)
        i += 1

def get_tangent(f, x_0):
    @lru_cache(maxsize=None)
    def f_cached(x):
        return f(x)
    f_xo = f_cached(x_0)
    der_f_xo = compute_derivative(f_cached, x_0)
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
    @lru_cache(maxsize=None)
    def f_cached(x):
        return f(x)
    if f_cached(a) == 0:
        return a
    if f_cached(b) == 0:
        return b
    while abs(b - a) > 0.0001:
        mid = (a + b) / 2
        if f_cached(mid) == 0:
            return mid
        if f_cached(a) * f_cached(mid) < 0:
            b = mid
        else:
            a = mid
    return round((a + b) / 2, 1)
