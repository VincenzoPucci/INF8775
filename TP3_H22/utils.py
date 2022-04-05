def compute_energy(solution, H, G):
    """Compute the total energy of a given solution
    solution: dictionnaire {node_id : atom type}
    H: List of list (matrix) of energy
    G: List of links (tuples)"""
    energy = 0
    for link in G:
        a = solution[link[0]]
        b = solution[link[1]]
        energy += H[a][b]
    return energy