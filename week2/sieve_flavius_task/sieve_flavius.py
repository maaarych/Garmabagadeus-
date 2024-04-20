'''HOMEWORK'''
def sieve_flavius(number: int) -> list[int]:
    '''
    int -> list[int]
    function made to return lucky numbers until they are bigger then number given
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    
    >>> sieve_flavius(300)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, \
99, 105, 111, 115, 127, 129, 133, 135, 141, 151, 159, 163, 169, 171, 189, 193, 195, 201,\
 205, 211, 219, 223, 231, 235, 237, 241, 259, 261, 267, 273, 283, 285, 289, 297]
    '''
    if isinstance(number, int):
        list_ = [j for j in range(1, number+1) if j%2 == 1]
        for j in list_[1:]:
            if j in list_:
                length = len(list_)
                for i in range(1, length+1):
                    if i%j == 0:
                        list_[i-1] = 0
                while 0 in list_:
                    list_.remove(0)
        return list_
    return None

if __name__ == '__main__':
    import doctest
    print(doctest.testmod(verbose=True))
