import time
from getopt import getopt
import sys

from brute import naive
from divide import divide
from threshold import threshold


def getBuilding(path):
    with open(path, 'r') as pointFile:
        pointList = []
        next(pointFile)
        for x in pointFile:
            a, b, c = (int(x) for x in x.split())
            pointList.append((a, b, c))
    return pointList


def main(argv):
    algoType = None
    pathFile = None
    showResults = False
    showTime = False

    opts, args = getopt(argv, "a:e:pt")
    for opt, arg in opts:
        if opt == "-a" and (arg == "brute" or arg == "recursif" or arg == "seuil"):
            algoType = arg
        elif opt == "-e":
            pathFile = arg
        elif opt == "-p":
            showResults = True
        elif opt == "-t":
            showTime = True

    if not algoType:
        print("argument -a invalid")
        return
    if not pathFile:
        print("argument -e missing")
        return

    points = getBuilding(pathFile)
    results = []
    if algoType == "brute":
        time_init = time.perf_counter()
        results = naive(points)
        time_fin = time.perf_counter()
        diff = time_fin - time_init

    elif algoType == "recursif":
        time_init = time.perf_counter()
        results = divide(points)
        time_fin = time.perf_counter()
        diff = time_fin - time_init

    elif algoType == "seuil":
        time_init = time.perf_counter()
        results = threshold(points, 20)
        time_fin = time.perf_counter()
        diff = time_fin - time_init

    if showTime:
        print(diff*1000)
    if showResults:
        for result in results:
            print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main(sys.argv[1:])
