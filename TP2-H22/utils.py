#permet d'avoir l'aire de la surface du bloc
def takeArea(bloc):
    return bloc[1]*bloc[2]


#Permet de savoir si un bloc fit sur un autre
def fitsOnBloc(base, top):
    return top[1] < base[1] and top[2] < base[2]