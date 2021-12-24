# 2019215049汪海涛
import numpy as np


def lagrange_interpolation(inter_point_list: list, input_num: float) -> float:
    inter_point_arr = np.array(inter_point_list)
    n = len(inter_point_arr)
    l_arr = np.zeros(n)
    for i in range(n):
        cur_x = inter_point_arr[i][0]
        denominator = 1
        molecule = 1
        for j in range(n - 1):
            molecule *= (input_num - inter_point_arr[(i + 1 + j) % n][0])
            denominator *= (cur_x - inter_point_arr[(i + 1 + j) % n][0])
        try:
            l_arr[i] = molecule / denominator
        except ZeroDivisionError:
            print(cur_x, molecule)
    res = 0
    for i in range(n):
        res += l_arr[i] * inter_point_arr[i][1]
    return res


def piecewise_lagrange_interpolation(inter_point_list: list,
                                     input_num: float) -> float:
    inter_point_arr = np.array(inter_point_list)
    inter_point_x_arr = np.transpose(inter_point_arr)[0]
    n = len(inter_point_x_arr)
    if input_num in inter_point_x_arr:
        return inter_point_arr[np.where(inter_point_x_arr == input_num)][1]
    else:
        for i in range(n - 1):
            if input_num > inter_point_x_arr[
                    i] and input_num < inter_point_x_arr[i + 1]:
                x_k = inter_point_arr[i][0]
                x_k_1 = inter_point_arr[i + 1][0]
                l_k = (input_num - x_k) / (x_k_1 - x_k)
                l_k_1 = (input_num - x_k_1) / (x_k - x_k_1)
                res = l_k * inter_point_arr[i][1] + l_k_1 * inter_point_arr[
                    i + 1][1]
                return res
            else:
                pass
        return None


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
