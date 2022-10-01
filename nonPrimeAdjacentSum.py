import math


class MyNode(object):

    def __init__(
        self,
        val=0,
        left=None,
        right=None,
        cost=0,
        ):
        self.val = val
        self.left = left
        self.right = right
        self.cost = cost


def is_prime(number):
    if number <= 1:
        return False
    my_value = round(math.sqrt(number))
    for i in range(2, my_value + 1):
        if is_prime(i):
            if number % i == 0:
                return False
    return True


def tree_constructor(
    _my_list,
    _my_root,
    i,
    j,
    ):
    _my_root.val = (-1 if is_prime(_my_list[i][j]) else _my_list[i][j])
    _my_root.cost = 0
    if i + 1 < len(_my_list):
        _my_root.left = MyNode()
        _my_root.right = MyNode()
        tree_constructor(_my_list, _my_root.right, i + 1, j + 1)
        tree_constructor(_my_list, _my_root.left, i + 1, j)


def cost_function(_my_root, _my_record, _my_rootcost):
    _my_root.cost = max(_my_rootcost + _my_root.val, _my_root.cost)
    if _my_root.left is not None and _my_root.left.val is not -1:
        _my_record = cost_function(_my_root.left, _my_record,
                                   _my_root.cost)
    if _my_root.right is not None and _my_root.right.val is not -1:
        _my_record = cost_function(_my_root.right, _my_record,
                                   _my_root.cost)
    if _my_root.left is None and _my_root.right is None:
        _my_record = max(_my_record, _my_root.cost)
    return _my_record


def main():
    filename = 'input.txt'
    my_file = open(filename, 'r')
    my_object = my_file.read().splitlines()
    output = 0
    my_list = []
    myroot = MyNode()

    for element in my_object:
        my_list.append([int(a) for a in element.split(' ')])
    tree_constructor(my_list, myroot, 0, 0)
    output = cost_function(myroot, output, myroot.cost)
    return output


print main()
