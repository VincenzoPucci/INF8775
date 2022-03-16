from glouton import glouton
from dynamique import dynamique
from tabou import tabou
from utils import takeArea, fitsOnBloc


def getBlocks(path):
    with open(path, 'r') as pointFile:
        pointList = []
        for x in pointFile:
            a, b, c = (int(x) for x in x.split())
            pointList.append((a, b, c))
    return pointList


def getHeight(blocList: list):
    height = 0
    for bloc in blocList:
        height += bloc[0]
    return height


def main():
    blocList = getBlocks("./tests/b100_1.txt")

    gloutonList = glouton(blocList.copy())
    #gloutonHeight = getHeight(gloutonList)
    # print(gloutonList)
    # print(gloutonHeight)

    #dynamList = dynamique(blocList.copy())
    #dynamHeight = getHeight(dynamList)
    # print(dynamList)
    # print(dynamHeight)

    tabouList = tabou(blocList.copy(), gloutonList.copy())
    print(tabouList)


if __name__ == "__main__":
    main()
