from distance import distance

"""
>>> distance(0, 0, 3, 4)
5.0
>>> distance(-1, -1, 2, 3)
4.0
>>> distance(5, 5, 5, 5)
0.0
>>> distance(0, 0, 0, 0)
0.0
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
