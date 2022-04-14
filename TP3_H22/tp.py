from bnb import branch_and_bound
from utils import compute_energy, print_sol, count_atomes_left
from glouton import glouton
from lasvegas import set_up


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


def main():
    t, k, A, nbAt, H, G = getData("Test1")

    nbLeft = 5
    #initial_sol = glouton(H.copy(), G.copy(), nbAt.copy(), nbLeft)
    for i in range(10):
        initial_sol, atomes_left, nodes_left = set_up(nbAt, t, 0)
        #atomes_left = count_atomes_left(initial_sol, k, nbAt)
        branch_and_bound(initial_sol, H, G, atomes_left, nodes_left)
    
    # DECOMMENTE POUR VOIR COMMENT LE GLOUTON MARCHE
    #t, k, A, nbAt, H, G = getData("N100_K3_0")
    #nbLeft = [10,10,10]  # Nombre d'atome qu'on veut qui reste après le glouton
    #solution = glouton(H.copy(), G.copy(), nbAt.copy(), nbLeft.copy())
    #print_sol(solution)
    #energy = compute_energy(solution, H, G)
    #print(energy)


if __name__ == "__main__":
    main()


""" Data types:
solution: dictionnaire {node_id : atom type}
H: List of list (matrix) of energy
G: List of links
"""
