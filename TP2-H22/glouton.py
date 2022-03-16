from utils import takeArea, fitsOnBloc


def glouton(blocList: list):
    towerList = []
    blocList.sort(reverse=True, key=takeArea)
    towerList.append(blocList[0])
    blocList.pop(0)
    for bloc in blocList:
        if fitsOnBloc(towerList[-1], bloc):
            towerList.append(bloc)
    return towerList
