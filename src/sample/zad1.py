class Hamming:
    """
    >>> hamming = Hamming()
    >>> hamming.distance('','')
    0
    >>> hamming.distance( 'A', '')
    Traceback (most recent call last):
    ...
    ValueError: Not equal lengths
    >>> hamming.distance( '', 'B')
    Traceback (most recent call last):
    ...
    ValueError: Not equal lengths
    >>> hamming.distance("A", "A")
    0
    >>> hamming.distance('C', '1')
    1
    >>> hamming.distance("ABCDEFFFFF", "ABCDEFFFFF")
    0
    >>> hamming.distance("GRACHAMKA", "GRAJDOLEK")
    6
    >>> hamming.distance('a','b')
    1
    >>> hamming.distance('a','bc')
    Traceback (most recent call last):
      ...
    ValueError: Not equal lengths
    >>> hamming.distance('a', 'A')
    1
    >>> hamming.distance('ac', 'a')
    Traceback (most recent call last):
      ...
    ValueError: Not equal lengths
    >>> hamming.distance(1,'12')
    Traceback (most recent call last):
        ...
    TypeError: object of type 'int' has no len()
    """
    def __init__(self):
        pass

    def distance(self, a, b):
        if len(a) == len(b):
            result = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    result += 1
                else:
                    pass
            return result
        else:
            raise ValueError("Not equal lengths")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
