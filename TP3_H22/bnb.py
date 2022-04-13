from utils import compute_energy, count_unused_link, print_sol

best_score = 1e25


def lower_bound(sol, H, G, atomes_left):
    """Compute lower bound on energy given an intermediate solution"""
    return compute_energy(sol, H, G) + sum([min(H[k]) * n for k, n in atomes_left.items()])


def branch_and_bound(initial_sol, H, G, atomes_left):
    best_sol = initial_sol.copy()
    nodes_left = [key for key, value in initial_sol.items() if value is None]
    
    def explore(initial_sol, H, G, atomes_left, nodes_left):
        global best_score
        if not(None in initial_sol.values()):
            energy = compute_energy(initial_sol, H, G)
            if energy < best_score:
                best_score = energy
                nonlocal best_sol
                best_sol = initial_sol

        else:
            current_node = nodes_left.pop()
            for k, n in atomes_left.items():
                if n > 0:
                    new_sol = initial_sol.copy() #pas très optimal si on doit copier à chaque fois
                    new_sol[current_node] = k
                    new_atomes_left = atomes_left.copy()
                    new_atomes_left[k] -= 1
                    if lower_bound(new_sol, H, G, new_atomes_left) < best_score:
                        print_sol(new_atomes_left)
                        explore(new_sol, H, G, new_atomes_left, nodes_left.copy())

    explore(initial_sol, H, G, atomes_left, nodes_left)
    print_sol(best_sol)
    print(best_score)