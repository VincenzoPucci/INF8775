import heapq

def make_critical_pt(list_building):
    list_critical = []
    for i, b in enumerate(list_building):
        list_critical.append([b[0], -b[2]])  # start point
        list_critical.append([b[1], b[2]])  # end point
    list_critical.sort()
    return list_critical


def naive(buildings):
    points = make_critical_pt(buildings)
    l = []
    heapq.heapify(l)
    heapq.heappush(l, 0)
    maxH = 0
    res = []
    for p in points:
        if p[1] < 0:
            heapq.heappush(l, p[1])
        else:
            for i, v in enumerate(l):
                if v == -p[1]:
                    del l[i]
                    heapq.heapify(l)
                    break
        if len(l) > 0 and maxH != l[0]:
            maxH = l[0]
            res.append([p[0], -maxH])
    return res

def naive_old(list_buildings):

    def is_in_building(pt, building):
        return pt[0] >= building[0] and pt[0] < building[1] and pt[1] <= building[2]

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
    return 