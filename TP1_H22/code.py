def make_critical_pt(list_building):
    list_critical = []
    for elem in list_building:
        list_critical.append((elem[0], elem[2]))
        list_critical.append((elem[1], 0))
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
                    x = list(crit)
                    x[1] = building[2]
                    crit = tuple(x)
        sol.append(crit)
        if idx != 0:
            if sol[-1][1] == sol[-2][1]:
                sol.pop()
    # print(sol)
    return sol


def divide(list_buildings):
    if len(list_buildings) == 1:
        return naive(list_buildings)
    else:
        sol1 = divide(list_buildings[:len(list_buildings)//2])
        sol2 = divide(list_buildings[len(list_buildings)//2:])
        return merge_2(sol1, sol2)


def merge(skl_1, skl_2):
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
        x = list(elem)
        x[1] = max(h1, h2)
        elem = tuple(x)
        sol.append(elem)
        if idx != 0:
            if sol[-1][1] == sol[-2][1]:
                sol.pop()
            elif sol[-1][0] == sol[-2][0]:
                min_h = min(sol[-1][1], sol[-2][1])
                sol.remove((sol[-1][0], min_h))
    return sol


def merge_2(skl_1, skl_2):
    h1 = 0
    h2 = 0
    sol = []
    i1 = 0
    i2 = 0
    while i1 < len(skl_1) and i2 < len(skl_2):
        if skl_1[i1][0] < skl_2[i2][0]:
            h1 = skl_1[i1][1]
            sol.append((skl_1[i1][0], max(h1, h2)))
            i1 += 1
        else:
            h2 = skl_2[i2][1]
            sol.append((skl_2[i2][0], max(h1, h2)))
            i2 += 1
    if i1 == len(skl_1):
        sol + skl_2[i2:]
    else:
        sol + skl_1[i1:]
    return sol


with open("N1000_0", 'r') as pointFile:
    pointList = []
    next(pointFile)
    for x in pointFile:
        a, b, c = (int(x) for x in x.split())
        pointList.append((a, b, c))
    d = naive(pointList[0:20])
    a = len(d)
    c = divide(pointList[0:20])
    print(d)
    print(c)
    b = len(c)
    print(a)
    print(b)
