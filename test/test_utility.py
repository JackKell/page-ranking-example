import unittest

import numpy
from numpy import matrix, array

from irhw2.utility import getMatrixFromText, getStochasticMatrix, getRandomSurferRanking


class TestGetStochasticMatrix(unittest.TestCase):
    def test_uniform_matrix_size_3(self):
        m: matrix = matrix([
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ])

        stochasticM = getStochasticMatrix(m)
        correctMatrix = m / 3

        self.assertTrue(numpy.array_equal(correctMatrix, stochasticM))

    def test_matrix_size_3(self):
        m: matrix = matrix([
            [1, 1, 1],
            [0, 1, 1],
            [0, 0, 1],
        ])

        stochasticM = getStochasticMatrix(m)
        correctMatrix = matrix([
            [1, 0.5, numpy.divide(1, 3)],
            [0, 0.5, numpy.divide(1, 3)],
            [0, 0, numpy.divide(1, 3)],
        ])

        self.assertTrue(numpy.array_equal(correctMatrix, stochasticM))


class TestGetRandomSurferRanking(unittest.TestCase):
    def test_3x3(self):
        inputMatrix: matrix = matrix(
            [
                [1, 1, 0],
                [1, 0, 1],
                [0, 1, 0]
            ])
        correctRanking: array = array(
            [
                numpy.divide(6, 15),
                numpy.divide(6, 15),
                numpy.divide(3, 15)
            ])
        outputRanking, firstRanking, iterations, transitionMatrix = getRandomSurferRanking(inputMatrix, 1, 0.85)
        self.assertTrue(numpy.array_equal(correctRanking, outputRanking))


class TestGetMatrixFromText(unittest.TestCase):
    def test_convert_from_example_graph_1(self):
        filePath: str = "../data/exampleGraph1.txt"
        generatedMatrix: matrix = getMatrixFromText(filePath)
        print(generatedMatrix)
        correctMatrix: matrix = matrix([
            [0, 1, 0],
            [1, 1, 0],
            [1, 1, 0]
        ])
        print(correctMatrix)
        self.assertTrue(numpy.array_equal(generatedMatrix, correctMatrix))
