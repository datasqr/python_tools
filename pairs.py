from itertools import combinations, product

"""
Function to create unique pairs of values from two lists
"""

def pairs(*lists):
    listToReturn = []
    listOfArgs = []
    for item in lists:
        listOfArgs.append(item)
    if len(listOfArgs) > 1:
        for t in combinations(lists, len(listOfArgs)):
            for pair in product(*t):
                listToReturn.append(pair)
    else:
        listToReturn = listOfArgs[0]

    return (listToReturn)

list1 = [1,2,3,4]
list2 = [5,6,7,8]

res = pairs(list1, list2)

print(res)
# [(1, 5), (1, 6), (1, 7), (1, 8), (2, 5), (2, 6), (2, 7), (2, 8), (3, 5), (3, 6), (3, 7), (3, 8), (4, 5), (4, 6), (4, 7), (4, 8)]
