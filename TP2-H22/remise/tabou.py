from utils import takeArea, fitsOnBloc, getHeight
from random import randint, seed

def getNeighbors(blockList, initial_solution):
    """returns list of neighbor solutions and list of tabou block of each neighbors"""
    tabouList = []
    neighborsList = []
    newBlock = list(set(blockList).difference(set(initial_solution)))
    for blocOut in newBlock:
        sol = initial_solution.copy() #initial solution
        sol_tabou = [] #tabou block of the current solution
        for blocIn in reversed(initial_solution):  #starting from the top of the solution
            if fitsOnBloc(blocIn, blocOut): #try to insert the block
                idxIn = sol.index(blocIn)+1
                sol.insert(idxIn, blocOut)
                while idxIn < len(sol)-1: #check if upper block are still legal
                    if not fitsOnBloc(sol[idxIn], sol[idxIn+1]):
                        sol_tabou.append(sol[idxIn])
                        sol.pop(idxIn)
                    else:
                        idxIn += 1
                neighborsList.append(sol)
                tabouList.append(sol_tabou)
                break
    return neighborsList, tabouList

def tabou(blockList, gloutonList):
    seed(10)
    #print(f'Original solution height is : {getHeight(gloutonList)}')
    bestNeighbor = gloutonList
    tabouList = [[] for i in range(11)] #acts as a waiting queue
    for i in range(100):
        #add "free" blocks from the tabou list bakc into the block list
        freeBlock = tabouList.pop(0)
        blockList.extend(freeBlock)

        currentHeight = getHeight(bestNeighbor)
        neighborsList, tabouSol = getNeighbors(blockList, bestNeighbor)
        neighborsHeight = [getHeight(n) for n in neighborsList]
        bestHeight = max(neighborsHeight)
        idx = neighborsHeight.index(bestHeight)

        if bestHeight > currentHeight: #if new solution is better
            bestNeighbor = neighborsList[idx] #update solution
            #assign a random number of iteration during which the blocks are tabou
            randomIdx = randint(6, 9)
            tabouBlock = tabouSol[idx] #tabou blocks of the new solution
            tabouList[randomIdx].extend(tabouBlock)
            #remove tabou blocks from liste of free blocks
            blockList = list(set(blockList) - (set(tabouBlock)))
        else:
            bestHeight = currentHeight
        tabouList.append([])
    #print(f'Best height is : {getHeight(bestNeighbor)}')
    return bestNeighbor