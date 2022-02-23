from collections import deque
import time
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

from brute import naive, naive_old
from divide import divide
from threshold import threshold


def print_results(result, option="-p", time=None):
    if option == "-p":
        for i in result:
            print(f"{i[0]} {i[1]}")
    elif option == "-t":
        print(time)
    else:
        print(f"Illegal argument {option}. Correct arguments are -p or -t")


def getBuilding(path):
    with open(path, 'r') as pointFile:
        pointList = []
        next(pointFile)
        for x in pointFile:
            a, b, c = (int(x) for x in x.split())
            pointList.append((a, b, c))
    return pointList


def solve_skyline(path, option="-p"):
    pointList = getBuilding(path)

    time_init = time.perf_counter()
    naive_old(pointList)
    time_fin = time.perf_counter()
    time_naive = time_fin - time_init

    time_init = time.perf_counter()
    divide(pointList)
    time_fin = time.perf_counter()
    time_divide = time_fin - time_init

    time_init = time.perf_counter()
    threshold(pointList, 20)
    time_fin = time.perf_counter()
    time_threshold = time_fin - time_init

    return time_naive, time_divide, time_threshold

def benchmark(list_size_sample, number_sample=1):
    list_time_naive = []
    list_time_divide = []
    list_time_thres = []

    for size_sample in list_size_sample:
        time_naive = 0
        time_divide = 0
        time_thres = 0
        for n in range(number_sample):
            t1, t2, t3 = solve_skyline(f"test/N{size_sample}_{n}", "-t")
            time_naive += t1
            time_divide += t2
            time_thres += t3
        # take the average time
        time_naive = time_naive / number_sample
        time_divide = time_divide / number_sample
        time_thres = time_thres / number_sample
        list_time_naive.append(time_naive)
        list_time_divide.append(time_divide)
        list_time_thres.append(time_thres)

    return list_time_naive, list_time_divide, list_time_thres


def write_performance(time_naive, time_divide, time_threshold):
    textfile = open("performance_brute.txt", "w")
    for element in time_naive:
        textfile.write(str(element) + "\n")
    textfile.close()

    textfile = open("performance_divide.txt", "w")
    for element in time_divide:
        textfile.write(str(element) + "\n")
    textfile.close()

    textfile = open("performance_thresh.txt", "w")
    for element in time_threshold:
        textfile.write(str(element) + "\n")
    textfile.close()

    #also plot overal performance:
    plt.figure()
    plt.scatter(list_size_sample, list_time_naive, label="bruteforce") 
    plt.scatter(list_size_sample, list_time_divide, label="divide") 
    plt.scatter(list_size_sample, list_time_threshold, label="threshold")
    plt.legend()
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("temps (sec)")
    plt.title("performance")
    plt.savefig("performance.png", format="png")
    plt.show()



def plot_puissance(list_time_naive, list_time_divide, list_time_threshold, list_size_sample):
    
    #bruteforce
    plt.figure()
    plt.scatter(list_size_sample, list_time_naive, label="bruteforce") 
    plt.yscale("log")
    plt.xscale("log")

    logA = np.log(list_size_sample)
    logB = np.log(list_time_naive)
    coeffs = np.polyfit(logA, logB, deg=1)
    poly = np.poly1d(coeffs)
    yfit = lambda x: np.exp(poly(np.log(x)))
    plt.loglog(list_size_sample, yfit(list_size_sample), color = 'red', label = f"régression linéaire: y = {np.around(poly[1], 2)}x + {np.around(poly[0], 2)}")

    plt.legend()
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("temps (sec)")
    plt.title("Test puissance")
    plt.savefig("puissance_brute.png", format="png")
    plt.show()

    #divide and conquer
    plt.figure()
    plt.scatter(list_size_sample, list_time_divide, label="divide and conquer") 
    plt.yscale("log")
    plt.xscale("log")

    logA = np.log(list_size_sample)
    logB = np.log(list_time_divide)
    coeffs = np.polyfit(logA, logB, deg=1)
    #PROBLEM HERE
    poly = np.poly1d(coeffs)
    yfit = lambda x: np.exp(poly(np.log(x)))
    plt.loglog(list_size_sample, yfit(list_size_sample), color = 'red', label = f"régression linéaire: y = {np.around(poly[1], 2)}x + {np.around(poly[0], 2)}")

    plt.legend()
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("temps (sec)")
    plt.title("Test puissance")
    plt.savefig("puissance_diviser.png", format="png")
    plt.show()

    #threshold
    plt.figure()
    plt.scatter(list_size_sample, list_time_threshold, label="divide and conquer with threshold") 
    plt.yscale("log")
    plt.xscale("log")

    logA = np.log(list_size_sample)
    logB = np.log(list_time_threshold)
    coeffs = np.polyfit(logA, logB, deg=1)
    poly = np.poly1d(coeffs)
    yfit = lambda x: np.exp(poly(np.log(x)))
    plt.loglog(list_size_sample, yfit(list_size_sample), color = 'red', label = f"régression linéaire: y = {np.around(poly[1], 2)}x + {np.around(poly[0], 2)}")

    plt.legend()
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("temps (sec)")
    plt.title("Test puissance")
    plt.savefig("puissance_seuil.png", format="png")
    plt.show()

def f(x, type):
        #for bruteforce
        if type == "brute":
            return np.square(x)
        #for divide and conquer or threshold
        elif type == "divide" or type == "thresh":
            return x * np.log2(x)
        else:
            print("error: f type not specified")
            return x

def plot_rapport(list_time_naive, list_time_divide, list_time_threshold, list_size_sample):

    for i, b in enumerate(list_time_naive):
        list_time_naive[i] = b/f(list_size_sample[i], "brute")
    plt.figure()
    plt.scatter(list_size_sample, list_time_naive, label="bruteforce")
    plt.legend()
    plt.ylim(bottom=0) 
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("rapport y/f(x)")
    plt.title("Test du rapport")
    plt.savefig("rapport_brute.png", format="png")
    plt.show()

    for i, b in enumerate(list_time_divide):
        list_time_divide[i] = b/f(list_size_sample[i], "divide")
    plt.figure()
    plt.scatter(list_size_sample, list_time_naive, label="divide and conquer")
    plt.legend()
    plt.ylim(bottom=0) 
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("rapport y/f(x)")
    plt.title("Test du rapport")
    plt.savefig("rapport_brute.png", format="png")
    plt.show()

    for i, b in enumerate(list_time_threshold):
        list_time_threshold[i] = b/f(list_size_sample[i], "thresh")
    plt.figure()
    plt.scatter(list_size_sample, list_time_threshold, label="divide and conquer with threshold")
    plt.legend()
    plt.ylim(bottom=0) 
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("rapport y/f(x)")
    plt.title("Test du rapport")
    plt.savefig("rapport_brute.png", format="png")
    plt.show()


def plot_constante(list_time_naive, list_time_divide, list_time_threshold, list_size_sample):

    plt.figure()
    fn = f(np.array(list_size_sample), type='brute')
    plt.scatter(fn, list_time_naive, label="bruteforce")
    x = np.linspace(0, fn[-1], 1000)
    m,b = np.polyfit(fn, list_time_naive, 1)
    plt.plot(x, m*x+b, color="red", label = f"régression linéaire: y = {np.format_float_scientific(m, 2)}x + {np.format_float_scientific(b, 2)}")
    plt.legend()
    plt.xlabel("f(n)")
    plt.ylabel("temps (sec)")
    plt.title("Test des constantes")
    plt.savefig("constante_brute.png", format="png")
    plt.show()

    plt.figure()
    fn = f(np.array(list_size_sample), type='divide')
    plt.scatter(fn, list_time_divide, label="divide and conquer")
    x = np.linspace(0, fn[-1], 1000)
    m,b = np.polyfit(fn, list_time_divide, 1)
    plt.plot(x, m*x+b, color="red", label = f"régression linéaire: y = {np.format_float_scientific(m, 2)}x + {np.format_float_scientific(b, 2)}")
    plt.legend()
    plt.xlabel("f(n)")
    plt.ylabel("temps (sec)")
    plt.title("Test des constantes")
    plt.savefig("constante_diviser.png", format="png")
    plt.show()

    plt.figure()
    fn = f(np.array(list_size_sample), type='thresh')
    plt.scatter(fn, list_time_threshold, label="divide and conquer with threshold")
    x = np.linspace(0, fn[-1], 1000)
    m,b = np.polyfit(fn, list_time_threshold, 1)
    plt.plot(x, m*x+b, color="red", label = f"régression linéaire: y = {np.format_float_scientific(m, 2)}x + {np.format_float_scientific(b, 2)}")
    plt.legend()
    plt.xlabel("f(n)")
    plt.ylabel("temps (sec)")
    plt.title("Test des constantes")
    plt.savefig("constante_seuil.png", format="png")
    plt.show()


if __name__ == "__main__":
    #list_size_sample = [500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    list_size_sample = [500, 1000, 5000, 10000]
    n_run = 1 #number of run for each sample size (averaged)
    list_time_naive, list_time_divide, list_time_threshold = benchmark(list_size_sample, n_run)

    #ouput runing time to txt
    write_performance(list_time_naive, list_time_divide, list_time_threshold)

    #plot test puissance
    plot_puissance(list_time_naive, list_time_divide, list_time_threshold, list_size_sample)

    #plot test constantes
    plot_constante(list_time_naive, list_time_divide, list_time_threshold, list_size_sample)

    #attention, toujours faire le test rapport après le test constantes !
    #plot test rapport
    plot_rapport(list_time_naive, list_time_divide, list_time_threshold, list_size_sample)




