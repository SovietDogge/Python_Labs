from my_multiset import MyMultiSet

if __name__ == '__main__':
    exm = MyMultiSet({3: 3, 1: 1, 2: 0})
    # print(exm.check_empty())
    # exm.add_num(3)
    # exm.add_num(1)
    # exm.add_num(3)
    # exm.add_num(3)
    # exm.clear()
    # print(exm.__dict__)
    tmp = MyMultiSet({3: 2, 2: 1, 4: 1, 1: 2})
    # tmp.add_num(3)
    # tmp.add_num(3)
    # tmp.add_num(2)
    # tmp.add_num(4)
    # tmp.add_num(1)
    # tmp.add_num(1)
    new_exmpl = exm.union(tmp)
    print(new_exmpl.__dict__)
