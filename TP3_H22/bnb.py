from utils import compute_energy, count_unused_link, print_sol
from glouton import glouton
import math

best_score = math.inf


def lower_bound(sol, H, G, atomes_left):
    """Compute lower bound on energy given an intermediate solution"""
    return compute_energy(sol, H, G) + sum([min(H[k]) * n for k, n in atomes_left.items()])


def branch_and_bound(initial_sol, H, G, atomes_left):
    nodes_left = [key for key, value in initial_sol.items() if value is None]
    
    def explore(initial_sol, H, G, atomes_left, nodes_left):
        global best_score
        if not(None in initial_sol.values()):
            energy = compute_energy(initial_sol, H, G)
            if energy < best_score:
                best_score = energy
                print(best_score, flush=True)

        else:
            current_node = nodes_left.pop()
            for k, n in atomes_left.items():
                if n > 0:
                    new_sol = initial_sol.copy() #pas très optimal si on doit copier à chaque fois
                    new_sol[current_node] = k
                    new_atomes_left = atomes_left.copy()
                    new_atomes_left[k] -= 1
                    if lower_bound(new_sol, H, G, new_atomes_left) < best_score:
                        explore(new_sol, H, G, new_atomes_left, nodes_left.copy())
    


    explore(initial_sol, H, G, atomes_left, nodes_left)
    print(best_score)