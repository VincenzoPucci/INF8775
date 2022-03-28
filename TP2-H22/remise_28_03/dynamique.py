from utils import takeArea, fitsOnBloc

def dynamique(blockList: list):
    blockList.sort(reverse=True, key=takeArea)
    H = [] #best tower height with block "i" on top
    last = [] #last block on which the current is sitting in the best configuration
    for i, block in enumerate(blockList):
        legalIndex = [] #list of index of blocks on which we can put the block
        for idx, prevBlock in enumerate(blockList[:i]):
            if fitsOnBloc(prevBlock, block):
                legalIndex.append(idx)
        if not legalIndex:
            last.append(None) #current block doesn't fit on previous blocks
            H.append(block[0])
        else:
            legalHeight = [H[j] for j in legalIndex]
            bestHeight = max(legalHeight)
            bestHeightIdx = H.index(bestHeight)
            H.append(bestHeight + block[0])
            last.append(bestHeightIdx)
    hmax = max(H)
    idx = H.index(hmax) #index of the block on top of the best tower
    result_inv = []
    while idx != None: #retrace the tower from top to bottom
        result_inv.append(blockList[idx])
        idx = last[idx]

    result = list(reversed(result_inv)) #result is bottom to top
    return result
