from utils import takeArea, fitsOnBloc


def glouton(blocList: list):
    towerList = []
    blocList.sort(reverse=True, key=takeArea)
    for bloc in blocList:
        if len(towerList) == 0:
            towerList.append(bloc)
        elif fitsOnBloc(towerList[-1], bloc):
            towerList.append(bloc)
    return towerList
