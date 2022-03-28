from utils import takeArea, fitsOnBloc


# On sort la liste pour que les bloc avec le plus grande aire soit en premier dans la liste,
# Permet de respecter l'idée de glouton de commencer par le plus gros jusqu'au plus petit
# J'ai pris l'aire car donnait les meilleurs résultats, j'ai essayer avec hauteur et le ration aire/ratio
def glouton(blocList: list):
    towerList = []
    blocList.sort(reverse=True, key=takeArea)
    towerList.append(blocList[0])
    blocList.pop(0)
    #on itère au travers de la liste et trouve les éléments qui fit sur le dernier bloc et construit la tour ainsi
    for bloc in blocList:
        if fitsOnBloc(towerList[-1], bloc):
            towerList.append(bloc)
    return towerList
