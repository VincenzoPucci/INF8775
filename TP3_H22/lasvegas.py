import random

def set_up(nbAt, t, n):
    initial_sol = {i: None for i in range(t)}
    atomes_left = {k: nbAt[k] for k in range(len(nbAt))}
    nodes_left = [i for i in range(t)]
    for i in range(n):
        atome = random.randint(0, len(nbAt)-1)
        if atomes_left[atome] > 0:
            site = random.choice(nodes_left)
            initial_sol[site] = atome
            atomes_left[atome] -= 1
            nodes_left.remove(site)
        else:
            pass
    return initial_sol, atomes_left, nodes_left
    
