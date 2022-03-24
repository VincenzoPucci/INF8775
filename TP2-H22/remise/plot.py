import matplotlib.pyplot as plt
import numpy as np

def nlogn(x):
    return x*np.log(x)

def n_pow3(x):
    return x**3

def n_2(x):
    return x**2

def test_rapport(time, sample_size, f, label):
    x = np.arange(0, max(sample_size))
    n = np.array(sample_size)
    f_n = f(n)
    rapport = np.array(time)/f_n
    c = 10

    fig = plt.figure()
    plt.plot(sample_size, rapport, 'ob')
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
    plt.title(label)
    plt.xlabel('log taille exemplaire')
    plt.ylabel(f'log consommation')
    plt.savefig(f'{label}.png')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    full_example_size = [100, 500, 1000]

    times = [[0.0003353499982040375, 0.03837472001905553, 1.1056947799981571], [0.0016419199877418579, 0.9923582699964755, 13.864413239993155], [0.0032874599855858833, 3.926810420001857, 38.429799999989335]]
    time_glouton = [t[0] for t in times]
    time_dyn = [t[1] for t in times]
    time_tabou = [t[2] for t in times]

    tower_size = [35.6, 83.7, 116.4]

    # test_rapport(time_glouton, full_example_size, nlogn, 'glouton')
    # test_puissance(time_dyn, full_example_size, 'dynamique')
    # test_rapport(time_tabou, full_example_size, n_2, 'tabou')
    #plt.plot(full_example_size, tower_size)
    #plt.show()




