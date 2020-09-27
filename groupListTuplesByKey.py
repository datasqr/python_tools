import itertools
import operator

def groupListTuplesByKey(list):
    it = itertools.groupby(list, operator.itemgetter(0))
    for key, subiter in it:
        yield key, [item[1] for item in subiter]
