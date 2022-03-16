def takeArea(bloc):
    return bloc[1]*bloc[2]


def fitsOnBloc(base, top):
    return top[1] < base[1] and top[2] < base[2]