from typing import Tuple

import numpy
from numpy import matrix, array, asarray, allclose, divide, repeat, zeros, genfromtxt


# Returns a new stochastic version of the input matrix
def getStochasticMatrix(inputMatrix: matrix, normZeros: bool = False) -> matrix:
    columnSums = asarray(inputMatrix.sum(0)).reshape(-1)
    if normZeros:
        for i in range(len(columnSums)):
            columnSum: float = columnSums[i]
            if columnSum == 0:
                inputMatrix[:, i] = 1
        return inputMatrix / inputMatrix.sum(0)
    else:
        columnSums[columnSums == 0] = 1
        return inputMatrix / columnSums


# Returns the node ranking of a given connection matrix using the random surfer model
def getRandomSurferRanking(connectionMatrix: matrix, decimals=1, beta: float = 0.85, normZeros: bool = False) -> \
        Tuple[array, array, int, matrix]:
    m = connectionMatrix.copy()
    nodeCount: int = m.shape[0]
    leapProbability: float = divide(1 - beta, nodeCount)
    m = getStochasticMatrix(m, normZeros)
    r: matrix = matrix(repeat(divide(1, nodeCount), nodeCount)).transpose()
    rZero: array = asarray(r).reshape(-1)
    previousR: matrix = zeros(r.shape)
    totalIterations: int = 0
    while not allclose(previousR, r, rtol=1.e-3, atol=1.e-3):
        previousR = r
        r = (beta * m * r) + leapProbability
        totalIterations += 1
    nodeRanking = asarray(r.round(decimals).transpose()).reshape(-1)
    return nodeRanking, rZero, totalIterations, m


# Returns a connection matrix from a text file in adjacency matrix format
def getMatrixFromText(fname: str) -> matrix:
    adjacencyMatrix: matrix = genfromtxt(fname, delimiter=" ", dtype=numpy.int64)
    maxIndex: int = adjacencyMatrix[:, 0:2].max()
    outputMatrix: matrix = zeros((maxIndex + 1, maxIndex + 1))
    for row in adjacencyMatrix:
        i, j, k = row
        outputMatrix[j, i] = k
    return outputMatrix
