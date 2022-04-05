best_score = 0


def branch_and_bound(initial_sol, H, G, actual_score):
    if is_full(initial_sol):
        best_score = score(initial_sol)
        return initial_sol
