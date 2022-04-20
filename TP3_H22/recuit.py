from time import time
from utils import compute_energy, print_sol
import random
import math


def recuit(solution, H, G, argument):
    best_score = compute_energy(solution, H, G)
    temperature = 10
    runtime = 180  # in seconds
    lam = 0.99
    energy = best_score
    temp_time = time()
    while True:
        neighbour, energy_neighbour = find_neighbours(solution, energy, H, G)
        if energy_neighbour < energy:
            solution = neighbour
            energy = energy_neighbour
        else:
            p = random.random()
            threshold = math.exp(-(energy_neighbour-energy)/temperature)
            if p < threshold:
                solution = neighbour
                energy = energy_neighbour

        #temperature = temperature
        if time() > temp_time + 1:
            temp_time = time()
            temperature = lam * temperature
        if energy < best_score:
            best_score = energy
            if argument:
                print_sol(solution)
            else:
                print(energy, flush=True)


def find_neighbours(sol, energy_sol, H, G):
    n1 = random.randint(0, len(sol)-1)
    n2 = random.randint(0, len(sol)-1)
    if n1 != n2:  # not interesting to swap a node with itself
        neighbour = sol.copy()
        # we swap two nodes
        neighbour[n1] = sol[n2]
        neighbour[n2] = sol[n1]
        energy_neighbour = compute_energy(neighbour, H, G)
        return neighbour, energy_neighbour
    else:
        return sol, energy_sol
