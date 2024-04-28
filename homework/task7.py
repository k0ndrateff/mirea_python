class Node:
    def __init__(self, ind: int, d=None):
        if d is None:
            d = {}
        self.ind = ind
        self.d = d

    def set_val(self, key, val):
        self.d[key] = val

    def get_val(self, lst: list):
        if isinstance(self.d[lst[self.ind]], Node):
            return self.d[lst[self.ind]].get_val(lst)
        return self.d[lst[self.ind]]


def main(x):
    n_0_0 = Node(2)

    n_1_0 = Node(1)

    n_2_0 = Node(0)
    n_2_1 = Node(0)
    n_2_2 = Node(0)

    n_3_0 = Node(4)
    n_3_1 = Node(3)
    n_3_2 = Node(4)
    n_3_3 = Node(3)

    n_0_0.set_val(1966, n_1_0)
    n_0_0.set_val(1995, 13)
    n_0_0.set_val(1982, 14)

    n_1_0.set_val('HY', n_2_0)
    n_1_0.set_val('TCL', n_2_1)
    n_1_0.set_val('COBOL', n_2_2)

    n_2_0.set_val(1970, 0)
    n_2_0.set_val(2004, n_3_0)
    n_2_0.set_val(2014, n_3_1)
    n_2_1.set_val(1970, n_3_2)
    n_2_1.set_val(2004, 7)
    n_2_1.set_val(2014, 8)
    n_2_2.set_val(1970, n_3_3)
    n_2_2.set_val(2004, 11)
    n_2_2.set_val(2014, 12)

    n_3_0.set_val('YANG', 1)
    n_3_0.set_val('RHTML', 2)
    n_3_1.set_val('METAL', 3)
    n_3_1.set_val('OPA', 4)
    n_3_2.set_val('YANG', 5)
    n_3_2.set_val('RHTML', 6)
    n_3_3.set_val('METAL', 9)
    n_3_3.set_val('OPA', 10)

    return n_0_0.get_val(x)

print(main([1970, 'COBOL', 1982, 'OPA', 'YANG']))
