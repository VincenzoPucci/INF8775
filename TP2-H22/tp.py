from glouton import glouton


def getBlocks(path):
    with open(path, 'r') as pointFile:
        pointList = []
        areaList = []
        for x in pointFile:
            a, b, c = (int(x) for x in x.split())
            pointList.append((a, b, c))
            areaList.append(b*c)
    return pointList, areaList


def getHeight(blocList: list):
    height = 0
    for bloc in blocList:
        height += bloc[0]
    return height


def main():
    blocList, areaList = getBlocks("./tests/b100_1.txt")
    gloutonList = glouton(blocList.copy())
    gloutonHeight = getHeight(gloutonList)
    print(gloutonHeight)


if __name__ == "__main__":
    main()
