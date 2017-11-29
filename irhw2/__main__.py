from numpy import matrix

from irhw2.utility import getRandomSurferRanking, getMatrixFromText


def main():
    inputMatrix: matrix = getMatrixFromText("../data/graph.txt")
    print(inputMatrix)

    # inputMatrix: matrix = matrix([
    #     [0, 1, 0, 0],
    #     [1, 0, 0, 1],
    #     [1, 0, 1, 1],
    #     [1, 1, 0, 0]
    # ])

    # print(getStochasticMatrix(matrix(graphData)))
    # print(getPageRank(graphData, 3))
    print(getRandomSurferRanking(inputMatrix, 3, beta=0.80))
    #
    # graphData = [
    #     [0, 0, 1, 1],
    #     [1, 0, 0, 0],
    #     [1, 1, 0, 1],
    #     [1, 1, 0, 0]
    # ]
    # print(getPageRank(graphData, 3))


if __name__ == '__main__':
    main()
