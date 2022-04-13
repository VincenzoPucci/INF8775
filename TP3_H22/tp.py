from bnb import branch_and_bound
from utils import compute_energy, print_sol
from glouton import glouton


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
    t, k, A, nbAt, H, G = getData("N100_K3_0")

    initial_sol = {key: None for key in range(t)}
    atomes_left = {i: nbAt[i] for i in range(k)}  
    branch_and_bound(initial_sol, H, G, atomes_left)

    #solution = glouton(H.copy(), G.copy(), nbAt.copy())
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
