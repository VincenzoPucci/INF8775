import sys
from getopt import getopt

from utils import count_atomes_left, count_nodes_left
from glouton import glouton
from recuit import recuit


def getData(path):
    t = 0  # nb d'atomes totals
    k = 0  # nb types d'atomes
    A = 0  # nb arretes
    nbAt = []  # liste nb atome de chaque type
    H = []  # matrice energie
    G = []  # liste des arretes

    with open(path, 'r') as graphFile:
        max = 0
        for idx, x in enumerate(graphFile):
            if x != "\n":
                if idx == 0:
                    t, k, A = (int(x) for x in x.split())
                    max = 4 + k

                elif idx == 2:
                    nbAt = list(int(x) for x in x.split())

                elif idx >= 4 and idx <= max:
                    line1 = list(int(x) for x in x.split())
                    H.append(line1)

                elif idx >= max + 1:
                    line = list(int(x) for x in x.split())
                    G.append(line)
    return (t, k, A, nbAt, H, G)


def main(argv):

    pathFile = None
    showSol = False

    opts, args = getopt(argv, "e:p")

    for opt, arg in opts:
        if opt == "-e":
            pathFile = arg
        elif opt == "-p":
            showSol = True
    
    if not pathFile:
        print("argument -e missing")
        return

    t, k, A, nbAt, H, G = getData(pathFile)

    initial_sol = glouton(H.copy(), G.copy(), nbAt.copy())
    atomes_left = count_atomes_left(initial_sol, k, nbAt)
    nodes_left = count_nodes_left(initial_sol)
    recuit(initial_sol, H, G, showSol)


if __name__ == "__main__":
    main(sys.argv[1:])


""" Data types:
solution: dictionnaire {node_id : atom type}
H: List of list (matrix) of energy
G: List of links
"""
