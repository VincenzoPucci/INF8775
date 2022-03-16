import imp
from utils import takeArea, fitsOnBloc

#On prend le dernier bloc ajouter dans results comme currentBloc
#On trouve ensuite le bloc qui a le plus grand aire qui fit sur currentBloc et on l'ajoute a results et l'enlève de blocList
# On construit la tour ainsi de façon récursive jusqu'à ce qui on ne trouve plus de bloc dans blocList qui fit sur currentBloc
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
