from glouton import glouton
from dynamique import dynamique
from tabou import tabou
from utils import takeArea, fitsOnBloc, getHeight


def getBlocks(path):
    with open(path, 'r') as pointFile:
        pointList = []
        for x in pointFile:
            a, b, c = (int(x) for x in x.split())
            pointList.append((a, b, c))
    return pointList


def main():
    blockList = getBlocks("./tests/b100_3.txt")
    gloutonList = glouton(blockList.copy())
    gloutonHeight = getHeight(gloutonList)
    #print(gloutonList)
    #print(gloutonHeight)

    dynamList = dynamique(blockList.copy())
    dynamHeight = getHeight(dynamList)
    #print(dynamList)
    #print(dynamHeight)

    tabouSol = tabou(blockList.copy(), gloutonList.copy())
    return tabouSol

if __name__ == "__main__":
    sol = main()
    for l in sol:
        print(str(l[0]) + " " + str(l[1]) + " " + str(l[2]))