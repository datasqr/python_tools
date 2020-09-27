
from collections import OrderedDict

def group_list(lst):
    lst1 = [item.upper() for item in lst]
    res = [(el, lst.count(el)) for el in lst1]
    return list(OrderedDict(res).items())
