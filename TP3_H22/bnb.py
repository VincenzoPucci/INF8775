from utils import compute_energy, count_unused_link


best_score = 0

def lower_bound(sol, H, G):
    """Compute lower bound on energy given an intermediate solution"""
    return compute_energy(sol) + min(H) * count_unused_link(sol, G)

def branch_and_bound(initial_sol, H, G):
    if None not in initial_sol:
        best_score = compute_energy(initial_sol)
        return initial_sol
    else:
        if lower_bound(initial_sol) < best_score:
            for site, type in initial_sol.values():
                if type ==None:
                    for k in len(H[0]):
                        new_sol = initial_sol.copy() #pas très optimal si on doit copier à chaque fois
                        new_sol[site] = k
                        branch_and_bound(new_sol, H, G)
        else:
            return None