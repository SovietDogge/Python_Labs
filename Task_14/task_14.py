from my_multiset import MyMultiSet

if __name__ == '__main__':
    exm = MyMultiSet()
    # print(exm.check_empty())
    exm.add_num(3)
    exm.add_num(1)
    exm.add_num(3)
    exm.add_num(3)
    tmp = MyMultiSet()
    tmp.add_num(3)
    tmp.add_num(3)
    tmp.add_num(2)
    tmp.add_num(4)
    tmp.add_num(1)
    tmp.add_num(1)
    new_exmpl = exm.intersection(tmp)
    # print(exm.__dict__)
