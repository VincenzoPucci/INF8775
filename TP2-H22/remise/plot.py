import matplotlib.pyplot as plt
import numpy as np

def nlogn(x):
    return x*np.log(x)

def n_pow4(x):
    return x**4

def test_rapport(time, sample_size, f, label):
    x = np.arrange(0, max(sample_size))
    n = np.array(sample_size)
    f_n = f(n)
    rapport = np.array(time)/f_n
    c = 10

    fig = plt.figure()
    plt.plot(sample_size, rapport, 'ob')
    plt.plot(x, c*x, '-r', label = f"y = {c}")
    plt.legend()
    plt.title(f"test rapport {label}/{f}")
    plt.xlabel('taille exemplaire')
    plt.ylabel(f'rapport consomation/{f}')
    plt.savefig(f'rapport_{label}_{f}.png')
    plt.show()

def test_puissance(time, sample_size, label):
    x = np.arrange(0, max(sample_size))

    plt.loglog(sample_size, time, 'ob')
    b, m = np.polyfit(sample_size, time, 1)
    plt.plot(x, m*x + b, '-r', label = f'y = {m}*x + {b}')
    plt.title(label)
    plt.xlabel('log taille exemplaire')
    plt.ylabel(f'log consommation')
    plt.savefig(f'{label}.png')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    full_example_size = [100, 500, 1000, 5000, 10000, 50000, 100000]

    time_glouton = []
    time_dyn = []
    time_tabou = []

    test_rapport(time_glouton, full_example_size, nlogn, 'glouton')
    test_puissance(time_dyn, full_example_size, 'dynamique')
    test_rapport(time_tabou, full_example_size, n_pow4, 'tabou')








