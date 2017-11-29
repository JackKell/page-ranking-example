from typing import List, Tuple

import numpy
from numpy import matrix, asarray, allclose, ndarray, divide, repeat, zeros, genfromtxt


# def getPageRank(connectionMatrix: matrix, decimals: int=1) -> Tuple[ndarray, int]:
#     return getRandomSurferRanking(connectionMatrix, decimals, 1.0)


def getStochasticMatrix(inputMatrix: matrix) -> matrix:
    columnSums = asarray(inputMatrix.sum(0)).reshape(-1)
    for i in range(len(columnSums)):
        columnSum: float = columnSums[i]
        if columnSum == 0:
            inputMatrix[:, i] = 1
    return inputMatrix / inputMatrix.sum(0)


def getRandomSurferRanking(connectionMatrix: matrix, decimals=1, beta: float = 0.85) -> Tuple[ndarray, int]:
    m = connectionMatrix.copy()
    nodeCount: int = m.shape[0]
    leapProbability: float = divide(1 - beta, nodeCount)
    m = getStochasticMatrix(m)
    r: matrix = matrix(repeat(divide(1, nodeCount), nodeCount)).transpose()
    previousR: matrix = zeros(r.shape)
    totalIterations: int = 0
    while not allclose(previousR, r):
        previousR = r
        r = (beta * m * r) + leapProbability
        totalIterations += 1
    nodeRanking = asarray(r.round(decimals).transpose()).reshape(-1)
    return nodeRanking, totalIterations


def getMatrixFromText(fname: str) -> matrix:
    adjacencyMatrix: matrix = genfromtxt(fname, delimiter=" ", dtype=numpy.int64)
    # minIndex: int = adjacencyMatrix[:, 0:2].min()
    maxIndex: int = adjacencyMatrix[:, 0:2].max()
    outputMatrix: matrix = zeros((maxIndex + 1, maxIndex + 1))
    for row in adjacencyMatrix:
        i, j, k = row
        outputMatrix[j, i] = k
    return outputMatrix
