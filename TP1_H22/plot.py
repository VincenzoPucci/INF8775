from collections import deque
import time
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

from brute import naive
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
    naive(pointList)
    time_fin = time.perf_counter()
    time_naive = time_fin - time_init

    time_init = time.perf_counter()
    divide(pointList)
    time_fin = time.perf_counter()
    time_divide = time_fin - time_init

    time_init = time.perf_counter()
    threshold(pointList, len(pointList)*0.3)
    time_fin = time.perf_counter()
    time_threshold = time_fin - time_init

    return time_naive, time_divide, time_threshold

def perf_threshold(list_size_sample, number_sample=1):
    list_time_naive = []
    list_time_divide = []
    list_time_thres = []

    for size_sample in list_size_sample:
        time_naive = 0
        time_divide = 0
        time_thres = 0
        for n in range(number_sample):
            t1, t2, t3 = solve_skyline(f"threshold/N{size_sample}_{n}", "-t")
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


def plot_performance():
    list_size_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20,
                        30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]
    list_time_naive, list_time_divide, list_time_threshold = perf_threshold(
        list_size_sample, 10)
    plt.loglog(list_size_sample, list_time_naive, label="brute_force")
    plt.loglog(list_size_sample, list_time_divide, label="divide_and_conquer")
    plt.loglog(list_size_sample, list_time_threshold, label="threshold")
    plt.legend()
    plt.xlabel("size_sample")
    plt.ylabel("time (sec)")
    plt.title("performance in function of sample size")
    plt.savefig("performance.png", format="png")
    plt.show()

def plot_puissance():
    #list_size_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20,
    #                    30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]
    list_size_sample = [500,1000, 5000, 10000, 50000, 100000, 500000]
    list_time_naive, list_time_divide, list_time_threshold = perf_threshold(
        list_size_sample, 5)
        
    plt.figure()
    plt.scatter(list_size_sample, list_time_threshold, label="Diviser pour regner avec seuil") 
    plt.yscale("log")
    plt.xscale("log")

    logA = np.log(list_size_sample)
    logB = np.log(list_time_threshold)
    coeffs = np.polyfit(logA, logB, deg=1)
    poly = np.poly1d(coeffs)
    yfit = lambda x: np.exp(poly(np.log(x)))
    plt.loglog(list_size_sample,yfit(list_size_sample), color = 'red', label = 'régression linéaire')

    plt.legend()
    plt.xlabel("taille de l'exemplaire")
    plt.ylabel("temps (sec)")
    plt.title("Test puissance")
    plt.savefig("performance.png", format="png")
    plt.show()

def plot_rapport():
    list_size_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20,
                        30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]
    list_time_naive, list_time_divide, list_time_threshold = perf_threshold(
        list_size_sample, 10)
    
    for i, b in enumerate(list_time_threshold):
        list_time_threshold[i] = b/(len(list_size_sample)*np.log2(len(list_size_sample)))

    plt.figure()
    plt.scatter(list_size_sample, list_time_threshold, label="diviser pour regner avec seuil")
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
    
    for i, b in enumerate(list_size_sample):
        list_size_sample[i] = b/(len(list_size_sample)*np.log2(len(list_size_sample)))

    plt.figure()
    plt.scatter(list_size_sample, list_time_threshold, label="diviser pour regner avec seuil")

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
    plot_constante()
