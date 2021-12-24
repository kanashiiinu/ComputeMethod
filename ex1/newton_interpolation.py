# 2019215049汪海涛
import numpy as np
import matplotlib.pyplot as plt

X = 0
Y = 1


def newton_interpolation(inter_point_list: list, input_num: float) -> float:
    point_arr = np.array(inter_point_list)
    point_num, v = point_arr.shape
    newton_table = np.zeros((point_num, point_num + 1), dtype=np.float64)
    #把点插入表中
    for point_n in range(0, point_num):
        newton_table[point_n][X] = point_arr[point_n][X]
        newton_table[point_n][Y] = point_arr[point_n][Y]
    newton_i, newton_j = newton_table.shape
    for j in range(2, newton_j):
        for i in range(j - 1, newton_i):
            y = (newton_table[i - 1][j - 1] - newton_table[i][j - 1])
            x = (newton_table[i - j + 1][0] - newton_table[i][0])
            newton_table[i][j] = y / x
    f_coefficient = np.zeros((newton_j - 1))
    for j in range(1, newton_j):
        f_coefficient[j - 1] = newton_table[j - 1][j]
    res = 0
    for i in range(newton_i, 0, -1):
        res = input_num * res + f_coefficient[i - 1]
    return res


if __name__ == "__main__":
    inter_point_list = [[1.0, 1.0], [4.0, 2.0], [9.0, 3.0]]
    input_num = 5.0
    print(newton_interpolation(inter_point_list, input_num))
    
""" 1
1
2
4
3
9 """
# for n in range(0,3):
#     interPointXList[n][X] = float(input())
#     interPointXList[n][Y] = float(input())

