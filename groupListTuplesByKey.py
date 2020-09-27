import itertools
import operator

def groupListTuplesByKey(list):
    list = sorted(list, key=lambda tup: tup[0])
    it = itertools.groupby(list, operator.itemgetter(0))
    for key, subiter in it:
        yield key, [item[1] for item in subiter]
