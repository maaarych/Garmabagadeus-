def neutralise(s1, s2):
    return ''.join([c if c == s2[i] else '0' for i, c in enumerate(s1)])