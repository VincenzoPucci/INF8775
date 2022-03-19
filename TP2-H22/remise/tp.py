import sys
from getopt import getopt
import time

from glouton import glouton
from dynamique import dynamique
from tabou import tabou
from utils import getHeight


def getBlocks(path):
    with open(path, 'r') as pointFile:
        pointList = []
        for x in pointFile:
            a, b, c = (int(x) for x in x.split())
            pointList.append((a, b, c))
    return pointList


def main(argv):
    algoType = None
    pathFile = None
    showBlocs = False
    showTime = False

    opts, args = getopt(argv, "a:e:pt")
    for opt, arg in opts:
        if opt == "-a" and (arg == "glouton" or arg == "progdyn" or arg == "tabou"):
            algoType = arg
        elif opt == "-e":
            pathFile = arg
        elif opt == "-p":
            showBlocs = True
        elif opt == "-t":
            showTime = True

    if not algoType:
        print("argument -a invalid")
        return
    if not pathFile:
        print("argument -e missing")
        return

    blockList = getBlocks(pathFile)

    if algoType == "glouton":
        time_init = time.perf_counter()
        result = glouton(blockList.copy())
        height = getHeight(result)
        time_fin = time.perf_counter()
        diff = time_fin - time_init

    elif algoType == "progdyn":
        time_init = time.perf_counter()
        result = dynamique(blockList.copy())
        height = getHeight(result)
        time_fin = time.perf_counter()
        diff = time_fin - time_init

    elif algoType == "tabou":
        time_init = time.perf_counter()
        gloutonList = glouton(blockList.copy())
        result = tabou(blockList.copy(), gloutonList.copy())
        height = getHeight(result)
        time_fin = time.perf_counter()
        diff = time_fin - time_init

    if showBlocs:
        for bloc in result:
            print(bloc)

    if showTime:
        print(diff*1000)


if __name__ == "__main__":
    main(sys.argv[1:])