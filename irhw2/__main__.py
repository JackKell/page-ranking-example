from typing import Tuple

from sys import argv
from numpy import matrix

from irhw2.utility import getRandomSurferRanking, getMatrixFromText


def main():
    inputFile: str = argv[1]
    inputConnectionMatrix: matrix = getMatrixFromText(inputFile)
    results: Tuple = getRandomSurferRanking(inputConnectionMatrix, 5, beta=0.85)
    ranking, rZero, iterations, transitionMatrix = results

    print("Connection Matrix")
    print(inputConnectionMatrix)
    print("Transition Matrix M:")
    print(transitionMatrix)
    print("Ranking at Iteration 0:")
    print(rZero)
    print("Converge Ranking at Iteration", iterations, ":")
    print(ranking)
    print("Total Iterations to reach convergence:", iterations)


if __name__ == '__main__':
    main()
