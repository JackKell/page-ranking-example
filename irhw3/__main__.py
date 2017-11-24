from typing import List, Tuple

import numpy
from numpy import matrix, asarray, allclose, ndarray


def getPageRank(graphData: List[List[int]], decimals: int=1) -> Tuple[ndarray, int]:
    return getRandomSurferRanking(graphData, decimals, 1)


def getRandomSurferRanking(graphData: List[List[int]], decimals: int=1, beta: float=0.85) -> Tuple[ndarray, int]:
    m: matrix = matrix(graphData)
    nodeCount = m.shape[0]
    # convert to stochastic adjacency matrix
    m = m / m.sum(0)
    # sum_i_j(beta * (r_i / d_j)) + (1 - beta) * (1 / n)
    m = m * beta + (1 - beta) * (1 / nodeCount)
    # m = m + (1 - beta) * (1 / nodeCount)
    r = matrix(numpy.repeat(1 / nodeCount, nodeCount)).transpose()
    previousR = numpy.zeros(r.shape)
    totalIterations = 0
    while not allclose(previousR, r):
        previousR = r
        r = (m * r)
        totalIterations += 1
    nodeRanking = asarray(r.round(decimals).transpose()).reshape(-1)
    return nodeRanking, totalIterations


def main():
    graphData = [
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    print(getPageRank(graphData, 3))
    print(getRandomSurferRanking(graphData, 3))

    graphData = [
        [0, 0, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0]
    ]
    print(getPageRank(graphData, 3))


if __name__ == '__main__':
    main()
