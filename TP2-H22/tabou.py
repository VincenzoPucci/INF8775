from utils import takeArea, fitsOnBloc


def tabou(blocList, gloutonList):
    tabouList = []
    results = gloutonList.copy()
    new = list(set(blocList).difference(set(gloutonList)))
    for blocOut in new:
        for blocIn in gloutonList:  # faut inverser gloutonList pour partir du top vers le bas
            if fitsOnBloc(blocIn, blocOut):
                idxIn = results.index(blocIn)+1
                results.insert(idxIn, blocOut)
                break

    return results
