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