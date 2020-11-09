class Calculate:
    def add(self, x, y):
        return x + y

    def addWithDocString(self, x, y):
        """Takes two integers and adds them together to produce the result
        # >>> c = Calculate()
        >>> c.addWithDocString(1,1)
        2
        >>> c.addWithDocString(25,125)
        150
        >>> c.addWithDocString(1.5656, 1.755)
        Traceback (most recent call last):
          File "/usr/lib/python3.8/doctest.py", line 1336, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest __main__.Calculate.addWithDocString[3]>", line 1, in <module>
            c.addWithDocString(1.5656, 1.755)
          File "DocTestExample.py", line 21, in addWithDocString
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))
        TypeError: Invalid type: <class 'float'> and <class 'float'>
        """
        if (type(x) == int and type(y) == int):
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))


if __name__ == "__main__":
    c = Calculate()
    print(c.add(2, 4))
    # print(c.addWithDocString(2.5, 4))
    print(Calculate.addWithDocString.__doc__)
    import doctest

    doctest.testmod()
    doctest.testmod(extraglobs={'c': Calculate()})
