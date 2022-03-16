import imp
from utils import takeArea, fitsOnBloc


def dynamicRecursive(blocList, currentBloc, results, hauteur):
    nextBlocID = -1
    maxArea = 0
    for j, bloc in enumerate(blocList):
        otherBloc = blocList[j]
        if fitsOnBloc(currentBloc, otherBloc):
            otherArea = otherBloc[1]*otherBloc[2]
            if otherArea > maxArea:
                maxArea = otherArea
                nextBlocID = j

    if fitsOnBloc(currentBloc, blocList[nextBlocID]):
        currentBloc = blocList[nextBlocID]
        results.append(currentBloc)
        blocList.pop(nextBlocID)
        hauteur += currentBloc[0]
        return dynamicRecursive(blocList, currentBloc, results, hauteur)
    else:
        return results


def dynamique(blocList: list):
    blocList.sort(reverse=True, key=takeArea)
    results = []
    results.append(blocList[0])
    currentBloc = blocList[0]
    blocList.pop(0)
    results = dynamicRecursive(blocList, currentBloc, results, currentBloc[0])
    return results
