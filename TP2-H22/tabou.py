from sklearn import neighbors
from utils import takeArea, fitsOnBloc, getHeight

def getNeighbors(blocList, initial_solution):
    """returns list of neighbor solutions and list of tabou block of each neighbors"""
    tabouList = []
    neighborsList = []
    newBlock = list(set(blocList).difference(set(initial_solution)))
    for blocOut in newBlock:
        sol = initial_solution.copy() #initial solution
        sol_tabou = [] #tabou block of the current solution
        for blocIn in reversed(initial_solution):  #starting from the top of the solution
            if fitsOnBloc(blocIn, blocOut): #try to insert the block
                idxIn = sol.index(blocIn)+1
                sol.insert(idxIn, blocOut)
                for i in range(idxIn+2, len(sol)): #remove upper blocks that doesn't fit anymore
                    if not fitsOnBloc(sol[i-1], sol[i]):
                        sol.pop(i)
                        sol_tabou.append(sol[i]) #add them to the solution's tabou list
                neighborsList.append(sol)
                tabouList.append(sol_tabou)
                break
    return neighborsList, tabouList

def tabou(blockList, gloutonList):
    
    neighborsList, tabouList = getNeighbors(blockList, gloutonList)
    neighborsHeight = [getHeight(n) for n in neighborsList]
    bestHeight = max(neighborsHeight)
    bestHeightIdx = neighborsHeight.index(bestHeight)
    #print(neighborsHeight)
    #print(f'Best height is : {bestHeight}')
    #print(f'Best neighbour index is : {bestHeightIdx}')
    #print(f'Original solution height is : {getHeight(gloutonList)}')
    return neighborsList[bestHeightIdx]