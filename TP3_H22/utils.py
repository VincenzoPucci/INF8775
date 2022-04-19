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

def count_atomes_left(sol, k, nb_atomes):
    atomes_count_sol = {i: list(sol.values()).count(i) for i in range(k)}
    atomes_left = {i: nb_atomes[i] - atomes_count_sol[i] for i in range(k)}
    return atomes_left

def count_nodes_left(sol):
    return [key for key, value in sol.items() if value is None]


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
    print(*dict_sol.values())
    #[print(i, end = ' ') for i in dict_sol.values()]
    #print("")