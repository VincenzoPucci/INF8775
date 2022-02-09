from collections import deque
import time
import matplotlib.pyplot as plt


def make_critical_pt(list_building):
    list_critical = []
    for elem in list_building:
        list_critical.append([elem[0], elem[2]])
        list_critical.append([elem[1], 0])
    list_critical.sort()
    return list_critical


def is_in_building(pt, building):
    return pt[0] >= building[0] and pt[0] < building[1] and pt[1] <= building[2]


def naive(list_buildings):
    list_critical = make_critical_pt(list_buildings)
    sol = []
    for idx, crit in enumerate(list_critical):
        for building in list_buildings:
            if is_in_building(crit, building):
                if crit[1] < building[2]:
                    crit[1] = building[2]
        sol.append(crit)
        if idx != 0:
            if sol[-1][1] == sol[-2][1]:
                sol.pop()
    # print(sol)
    return sol

def merge(skl_1, skl_2):
        elevated = deque([False,False])
        skl = skl_1 + skl_2
        skl.sort()
        h1 = 0
        h2 = 0
        sol = []
        for idx, elem in enumerate(skl):
            if elem in skl_1:
                h1 = elem[1]
            else:
                h2 = elem[1]
            #check if we must "elevate" the height of the point
            elevated.pop()
            if max(h1, h2) != elem[1]:
                elem[1] = max(h1, h2)
                elevated.appendleft(True)
            else:
                elevated.appendleft(False)
            sol.append(elem)
            if idx != 0:
                if sol[-1][1] == sol[-2][1]: #same height
                    sol.pop()
                elif sol[-1][0] == sol[-2][0]: #same x coordinate
                    min_h = min(sol[-1][1], sol[-2][1])
                    if elevated[-1] == True and len(sol) >= 2:
                        sol.remove(sol[-2])
                    else:
                        sol.remove([sol[-1][0], min_h]) #remove the smallest height
                    
        sol[-1][1] = 0
        return sol

def divide(list_buildings, threshold = 1):
    
    if len(list_buildings) <= threshold:
        return naive(list_buildings)
    else:
        sol1 = divide(list_buildings[:len(list_buildings)//2])
        sol2 = divide(list_buildings[len(list_buildings)//2:])
        return merge(sol1, sol2)

def print_results(result, option = "-p", time = None):
    if option == "-p":
        for i in result:
            print(f"{i[0]} {i[1]}")
    elif option == "-t":
        print(time)
    else:
        print(f"Illegal argument {option}. Correct arguments are -p or -t")


def solve_skyline(path, option = "-p"):
    with open(path, 'r') as pointFile:
        pointList = []
        next(pointFile)
        for x in pointFile:
            a, b, c = (int(x) for x in x.split())
            pointList.append((a, b, c))
    
    time_init = time.perf_counter()
    result_naive = naive(pointList)
    time_fin = time.perf_counter()
    time_naive = time_fin - time_init
    #print_results(result_naive, option, time_naive)

    time_init = time.perf_counter()
    result_divide = divide(pointList)
    time_fin = time.perf_counter()
    time_divide = time_fin - time_init
    #print_results(result_divide, option, time_divide)

    return time_naive, time_divide

    #check if both algorithms return same answer
    #print(result_naive == result_divide)
    #print([result_divide.index(item) for item in result_divide if item not in result_naive])

def perf_threshold(list_size_sample, number_sample = 1):
    list_time_naive = []
    list_time_divide = []

    for size_sample in list_size_sample:
        time_naive = 0
        time_divide = 0
        for n in range(number_sample):
            t1, t2 = solve_skyline(f"threshold/N{size_sample}_{n}", "-t")
            time_naive += t1
            time_divide += t2
        #take the average time
        time_naive = time_naive / number_sample
        time_divide = time_divide / number_sample
        list_time_naive.append(time_naive)
        list_time_divide.append(time_divide)

    return list_time_naive, list_time_divide

def plot_performance():
    list_size_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]
    list_time_naive, list_time_divide = perf_threshold(list_size_sample, 10)
    plt.loglog(list_size_sample, list_time_naive, label = "brute_force")
    plt.loglog(list_size_sample, list_time_divide, label = "divide_and_conquer")
    plt.legend()
    plt.xlabel("size_sample")
    plt.ylabel("time")
    plt.title("performance in function of sample size")
    plt.savefig("performance.pdf", format = "pdf")
    plt.show()

if __name__ == '__main__':

    plot_performance()

    # sizes = {"1000","5000","10000","50000","100000","500000"}
    # n_samples = 5
    # for n in range(n_samples):
    #     for s in sizes:
    #         solve_skyline(f"./test/N{s}_{n}")