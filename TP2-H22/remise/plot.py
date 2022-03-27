import matplotlib.pyplot as plt
import numpy as np

def nlogn(x):
    return x*np.log(x)

def n_pow3(x):
    return x**3/1e5

def n_2(x):
    return x**2

def test_rapport(time, sample_size, f, label):
    x = np.arange(0, max(sample_size))
    n = np.array(sample_size)
    f_n = f(n)
    rapport = np.array(time)/f_n
    c = 10

    fig = plt.figure()
    plt.plot(sample_size, rapport, 'ob', label = label)
    #plt.plot(x, c*np.ones(len(x)), '-r', label = f"y = {c}")
    plt.legend()
    plt.title(f"test rapport {label}")
    plt.xlabel('taille exemplaire')
    plt.ylabel(f'rapport consomation')
    plt.savefig(f'rapport_{label}.png')
    plt.show()

def test_puissance(time, sample_size, label):
    x = np.arange(0, max(sample_size))

    plt.loglog(sample_size, time, 'ob')
    logA = np.log(sample_size)
    logB = np.log(time)
    coeffs = np.polyfit(logA, logB, deg=1)
    poly = np.poly1d(coeffs)
    def yfit(x): return np.exp(poly(np.log(x)))
    plt.loglog(sample_size, yfit(sample_size), '-r', label = f"régression linéaire: y = {np.around(poly[1], 2)}x + {np.around(poly[0], 2)}")
    plt.title(f'test puissance {label}')
    plt.xlabel('log taille exemplaire')
    plt.ylabel(f'log consommation')
    plt.savefig(f'puissance_{label}.png')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    full_example_size = [100, 500, 1000, 5000, 10000]
    glouton_example_size = [100, 500, 1000, 5000, 10000, 50000]

    times = [[0.00031412001117132605, 0.0384246300032828, 1.08791016000323], [0.0018431499949656427, 0.9299275799945462, 13.387034240009962], [0.003835029999027029, 3.8469614399946295, 38.99465414001024], [0.0204482399916742, 114.97462790000137, 531.69224045999], [0.05190162999206223, 644.3122477500117, 1354.2938427500078]]
    #time_glouton = [t[0] for t in times]
    time_glouton = [0.0003322900156490505, 0.0010913899983279406, 0.0026745099981781094, 0.022384649998275562, 0.04086865000426769, 0.26108213999541474]

    time_dyn = [t[1] for t in times]
    time_tabou = [t[2] for t in times]

    tower_size = [[35.2, 38.1, 35.6], [82.3, 88.1, 83.7], [118.2, 127.8, 116.4], [268.2, 300.4, 268.0], [383.0, 425.5, 382.1]]
    tabou_tower_size = [t[2] for t in tower_size]

    test_rapport(time_glouton, glouton_example_size, nlogn, 'glouton')
    test_puissance(time_dyn, full_example_size, 'dynamique')
    test_puissance(time_tabou, full_example_size, 'tabou')
    plt.plot(full_example_size, tower_size, label = ['glouton', 'prog_dyn', 'tabou'])
    plt.legend()
    plt.savefig('tower_size')
    plt.show()
    test_puissance(tabou_tower_size, full_example_size, 'tower_size_tabou')




