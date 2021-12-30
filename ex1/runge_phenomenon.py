import matplotlib.pyplot as plt
from interpolation_fitting import *
from newton_interpolation import *

if __name__ == "__main__":
    n = 11
    inter_point_list = [[-5.0, 0], [-4.0, 0], [-3.0, 0], [-2.0, 0], [-1.0, 0],
                        [0.0, 0], [1.0, 0], [2.0, 0], [3.0, 0], [4.0, 0],
                        [5.0, 0]]
    for point in inter_point_list:
        point[1] = 1 / (1 + point[0] * point[0])

    input_num = 4.5
    print(lagrange_interpolation(inter_point_list, input_num))
    print(piecewise_lagrange_interpolation(inter_point_list, input_num))
