def getData(path):
    with open(path, 'r') as graphFile:
        pointList = []
        # next(graphFile)
        for x in graphFile:
            a, b, c = (int(x) for x in x.split())
            pointList.append((a, b, c))
    return 1


def main():
    getData("N5_K3_0")


if __name__ == "__main__":
    main()


""" Data types:
solution: dictionnaire {node_id : atom type}
H: List of list (matrix) of energy
G: List of links
"""