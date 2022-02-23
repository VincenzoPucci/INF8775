from collections import deque
import time
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

from remise.brute import naive, naive_old
from remise.divide import divide
from remise.threshold import threshold


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
    threshold(pointList, len(pointList)*0.3) #c'est bizzare comme threshold, j'aurai mis une cte...
    time_fin = time.perf_counter()
    time_threshold = time_fin - time_init

    return time_naive, time_divide, time_threshold

def perf_threshold(list_size_sample, number_sample=1):
    #each n sublist contains a samples for each size
    list_time_naive = []
    list_time_divide = []
    list_time_thres = []

    for n in range(number_sample):
        time_naive = []
        time_divide = []
        time_thres = []
        for size_sample in list_size_sample:
            t1, t2, t3 = solve_skyline(f"test/N{size_sample}_{n}", "-t")
            time_naive.append(t1)
            time_divide.append(t2)
            time_thres.append(t3)
        
        list_time_naive.append(time_naive)
        list_time_divide.append(time_divide)
        list_time_thres.append(time_thres)

    return list_time_naive, list_time_divide, list_time_thres


def plot_performance():
    nb_sample = 10
    list_size_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20,
                        30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]
    list_time_naive, list_time_divide, list_time_threshold = perf_threshold(
        list_size_sample, nb_sample)
    plt.loglog(list_size_sample[0], list_time_naive, label="brute_force")
    plt.loglog(list_size_sample[0], list_time_divide, label="divide_and_conquer")
    plt.loglog(list_size_sample[0], list_time_threshold, label="threshold")
    plt.legend()
    plt.xlabel("size_sample")
    plt.ylabel("time (sec)")
    plt.title("performance in function of sample size")
    plt.savefig("performance.png", format="png")
    plt.show()

def plot_puissance():
    #list_size_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20,
    #                    30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]
    list_size_sample = [500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    list_time_naive, list_time_divide, list_time_threshold = perf_threshold(
        list_size_sample, 1)
        
    plt.figure()
    plt.scatter(list_size_sample, list_time_divide, label="Diviser_pour_regner") 
    plt.yscale("log")
    plt.xscale("log")

    logA = np.log(list_size_sample)
    logB = np.log(list_time_divide)
    coeffs = np.polyfit(logA, logB, deg=1)
    poly = np.poly1d(coeffs)
    yfit = lambda x: np.exp(poly(np.log(x)))
    plt.loglog(list_size_sample, yfit(list_size_sample), color = 'red', label = f"régression linéaire: y = {np.around(poly[1], 2)}x + {np.around(poly[0], 2)}")

    plt.legend()
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("temps (sec)")
    plt.title("Test puissance")
    plt.savefig("puissance_diviser.png", format="png")
    plt.show()

def f(x, type = "brute"):
        #for bruteforce
        if type == "brute":
            return np.square(x)
        #for divide and conquer or threshold
        elif type == "divide" or type == "thresh":
            return x * np.log2(x)
        else:
            print("error: f type not specified")
            return x

def plot_rapport():
    #list_size_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20,
    #                    30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]
    list_size_sample = [500, 1000, 5000, 10000, 50000, 100000]
    list_time_naive, list_time_divide, list_time_threshold = perf_threshold(
        list_size_sample, 1)
    
    for i, b in enumerate(list_time_naive):
        list_time_naive[i] = b/f(list_size_sample[i], "brute")

    for i, b in enumerate(list_time_divide):
        list_time_divide[i] = b/f(list_size_sample[i], "divide")

    plt.figure()
    plt.scatter(list_size_sample, list_time_divide, label="diviser pour regner")
    plt.scatter(list_size_sample, list_time_naive, label="bruteforce")

    plt.legend()
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("temps (sec)")
    plt.title("Test du rapport")
    plt.savefig("performance.png", format="png")
    plt.show()


def plot_constante():
    list_size_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_time_naive, list_time_divide, list_time_threshold = perf_threshold(
        list_size_sample, 10)
    
    plt.figure()
    plt.scatter(f(np.array(list_size_sample)), list_time_threshold, label="diviser pour regner avec seuil")

    m,b = np.polyfit(list_size_sample, list_time_threshold, 1)
    x= np.array(list_size_sample)
    plt.plot(list_size_sample,m*x+b, color="red")
    plt.legend()
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("temps (sec)")
    plt.title("Test des constantes")
    plt.savefig("performance.png", format="png")
    plt.show()

if __name__ == "__main__":
    plot_rapport()
