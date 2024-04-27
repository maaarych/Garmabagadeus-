'''homework'''
import time
def factorial_recursive(n):
    '''
    function to count factorial of n
    >>> factorial_recursive(9)
    362880
    '''
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    '''
    function to count factorial of n
    >>> factorial_recursive(9)
    362880
    '''
    result=1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial_iterative(9))

def fibonacci_recursive(n):
    '''
    function to compute the n Fibonacci number.
    >>> fibonacci_recursive(5)
    8
    '''
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    '''
    function to compute the n Fibonacci number.
    >>> fibonacci_iterative(6)
    8
    '''
    lst = [1, 1]
    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst[-1]

def time_test(function, verbose=False):
    """
    measure the work time of a given function.
    """
    start_time = time.time()
    result = function(30)
    end_time = time.time()
    execution_time = end_time - start_time

    if verbose:
        print(f"Result: {result}")
        print(f"Execution Time: {execution_time} seconds")

    return execution_time

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())