import numpy as np
import matplotlib.pyplot as plt


class FitFunction():
    def __init__(self) -> None:
        pass

    def curret_func(self, x: float) -> float:
        return self.sin_div_x(x)

    def sin_div_x(self, x: float) -> float:
        return np.sinc(x / np.pi)


def trapezoidal_recurrence_formula_n(a: float, b: float,
                                     inter_point_x_list: list):
    inter_point_x_arr = np.array(inter_point_x_list)
    point_x_end = inter_point_x_arr.shape[0]
    h = b - a
    h_index = point_x_end - 1 - 0
    T_k = (inter_point_x_arr[0] + inter_point_x_arr[point_x_end - 1]) / 2
    T_2k = 0
    T_list = []
    T_list.append(T_k)
    while(int(h_index)>1):
        s = 0
        x_index = h_index / 2
        while True:
            s += inter_point_x_arr[int(x_index)]
            x_index += h_index
            if x_index >= point_x_end - 1:
                break
            else:
                pass
        T_2k = T_k / 2 + h * s / 2
        T_list.append(T_2k)
        T_k = T_2k
        h_index /= 2
        h /= 2
    return T_list


def trapezoidal_recurrence_formula_tolerance_error(
        a: float, b: float, cur_fn: FitFunction,
        tolerance_error: float) -> list:
    h = b - a
    T_k = (cur_fn.curret_func(b) + cur_fn.curret_func(a)) / 2
    T_2k = 0
    T_list = []
    T_list.append(T_k)
    while True:
        s = 0
        x = a + h / 2
        while True:
            s += cur_fn.curret_func(x)
            x += h
            if x >= b:
                break
            else:
                pass
        T_2k = T_k / 2 + h * s / 2
        T_list.append(T_2k)
        if abs(T_2k - T_k) < tolerance_error:
            break
        else:
            T_k = T_2k
            h /= 2
    return T_list


def romberg_algorithm(inter_point_x_list: list,
                      a: float, b: float,tolerance_error:float):
    inter_point_x_list = trapezoidal_recurrence_formula_n(
        a, b, inter_point_x_list)

    point_num = len(inter_point_x_list)
    romberg_table = np.zeros((point_num, point_num-1), dtype=np.float64)
    #把点插入表中
    for point_n in range(0, point_num):
        romberg_table[point_n][0] = inter_point_x_list[point_n]
    romberg_i, romberg_j = romberg_table.shape
    coefficient = []
    for i in range(1,romberg_j):
        coefficient_val = 1
        for j in range(romberg_j - i,romberg_j,):
             coefficient_val *= 4
        coefficient.append(coefficient_val) 
    for j in range(1, romberg_j):
        for i in range(j, romberg_i):
            molecule = (coefficient[j-1] * romberg_table[i][j - 1] - romberg_table[i - 1][j - 1])
            denominator = coefficient[j-1] - 1
            romberg_table[i][j] = molecule / denominator
            if j == 3 and i > 3:
                r_k_1 = romberg_table[i][j]
                r_k = romberg_table[i-1][j]
                if abs(r_k_1 - r_k) < tolerance_error :
                    print(r_k)
                    break
    return romberg_table,r_k

if __name__ == "__main__":
    a = 0.0
    b = 1.0
    tolerance_error = 1e-7
    cur_fn = FitFunction()
    inter_point_x_list = []
    # n = 2**k
    k = 4
    inter_point_x_list = np.sinc(np.linspace(a, b, 2**k + 1) / np.pi).tolist()
    print(inter_point_x_list)
    print(trapezoidal_recurrence_formula_n(a,b,inter_point_x_list))
    print(trapezoidal_recurrence_formula_tolerance_error(a,b,cur_fn,tolerance_error))
    print(romberg_algorithm(inter_point_x_list, a, b,tolerance_error))
