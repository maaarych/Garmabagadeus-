def move_zeros(array):
    result = [i for i in array if i != 0]
    result.extend([0] * array.count(0))
    return result