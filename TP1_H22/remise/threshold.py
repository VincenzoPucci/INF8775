from brute import naive
from divide import merge


def threshold(list_buildings, limit):
    n = len(list_buildings)

    if n == 0:
        return []
    if n <= limit:
        return naive(list_buildings)
    if n == 1:
        return naive(list_buildings)
    
    left_skyline = threshold(list_buildings[: n // 2], limit)
    right_skyline = threshold(list_buildings[n // 2:], limit)

    return merge(left_skyline, right_skyline)
