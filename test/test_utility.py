import unittest

from numpy import matrix, int64

from irhw2.utility import getMatrixFromText


class TestGetStochasticMatrix(unittest.TestCase):
    def test_3x3(self):
        pass

    def test_4x4(self):
        pass


class TesGetRandomSurferRanking(unittest.TestCase):
    def test_3x3(self):
        pass

    def test_4x4(self):
        pass


class TestGetMatrixFromText(unittest.TestCase):
    def test_convert_from_example_graph_1(self):
        filePath: str = "../data/exampleGraph1.txt"
        adjacencyMatrix: matrix = getMatrixFromText(filePath)
        print(adjacencyMatrix)
        actualMatrix: matrix = matrix([
            [0, 1, 0],
            [1, 1, 0],
            [1, 1, 0]
        ], int64)
        print(actualMatrix)
        self.assertEqual(adjacencyMatrix, actualMatrix)

