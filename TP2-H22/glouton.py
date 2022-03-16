def takeArea(bloc):
    return bloc[1]*bloc[2]


def glouton(blocList: list):
    towerList = []
    blocList.sort(reverse=True, key=takeArea)
    for bloc in blocList:
        if len(towerList) == 0:
            towerList.append(bloc)
        elif bloc[1] < towerList[-1][1] and bloc[2] < towerList[-1][2]:
            towerList.append(bloc)
    return towerList
