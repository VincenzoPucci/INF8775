def compute_energy(solution, H, G):
    """Compute the total energy of a given solution
    solution: dictionnaire {node_id : atom type}
    H: List of list (matrix) of energy
    G: List of links (tuples)"""
    energy = 0
    for link in G:
        a = solution[link[0]]
        b = solution[link[1]]
        if a != None and b != None:
            energy += H[a][b]
    return energy


def count_unused_link(solution, G):
    nb = 0
    for link in G:
        a = solution[link[0]]
        b = solution[link[1]]
        if a == None or b == None:
            nb += 1
    return nb


# Gets sum of all the lines of the energy matrice
def getLineVal(H):
    valAt = []
    for list in H:
        val = 0
        for i in list:
            val += i
        valAt.append(val)
    return valAt

def print_sol(dict_sol):
    [print(i, end = ' ') for i in dict_sol.values()]
    print("")