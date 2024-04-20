def is_pangram(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    return len(set(s)) == 26