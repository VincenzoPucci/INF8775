from utils import getLineVal


def getPositionList(G):
    positionDict = {}
    for i in G:
        a = i[0]
        b = i[1]
        try:
            positionDict[a] += 1
        except:
            positionDict.update({a: 1})
        try:
            positionDict[b] += 1
        except:
            positionDict.update({b: 1})
    return (sorted(positionDict.items(),
                   key=lambda item: item[1], reverse=True))


def glouton(H, G, nbAt, nbLeft):
    valAt = getLineVal(H)
    positionList = getPositionList(G)
    size = len(positionList) - nbLeft
    
    solution = {}
    for idx, val in enumerate(positionList):
        index_min = None
        pos = val[0]
        if idx < size:
            index_min = min(range(len(valAt)), key=valAt.__getitem__)
            nbAt[index_min] -= 1
            if nbAt[index_min] < 0:
                found = False
                while found == False:
                    valAt[index_min] = 10000000
                    index_min = min(range(len(valAt)), key=valAt.__getitem__)
                    nbAt[index_min] -= 1
                    if nbAt[index_min] >= 0:
                        found = True
        solution.update({pos: index_min})

    solution = dict(sorted(solution.items(),
                           key=lambda item: item[0]))
    return solution
