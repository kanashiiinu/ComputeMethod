import pytest
import sys
from os.path import dirname, abspath
path = dirname(dirname(abspath(__file__)))
sys.path.append(path)
from ex5.gauss_elimination_method import *

import numpy as np


class TestGaussEliminationComputeDeterminant:
    def test_gauss_elimination_compute_determinant(self):
        A_list = [[3.0, -2.0, 1.0, 4.0], 
                  [-7.0, 5.0, -3.0, -6.0],
                  [2.0, 1.0, -1.0, 3.0], 
                  [4.0, -3.0, 2.0, 8.0]]
        assert abs(gauss_elimination_compute_determinant(A_list) - np.linalg.det(A_list)) < 1e-6


if __name__ == '__main__':
    pytest.main()
