import numpy as np
import matplotlib.pyplot as plt



class Function():
    def cur_fun(self, x: float, y: float):
        return self.ex_func(x, y)

    def ex_func(self, x: float, y: float):
        res = y - (2 * x) / y
        return res

    def book_p124_3(self, x: float, y: float):
        """assure x >= 0 and x <= 4,please"""
        assert x >= 0 and x <= 4
        res = 1 / (1 + x * x) - 2 * y * y
        return res

def get_segmented_interval(a:float,b:float,h:float) -> list:
    """请确保区间能被整除"""
    n = round((b - a) / h) + 1
    return np.linspace(a, b, n).tolist()
    

def init_array(y0: float, point_x_list: list):
    differential_array = np.zeros((2, len(point_x_list)))
    differential_array[0] = np.array(point_x_list)
    differential_array[1][0] = y0
    differential_array = np.transpose(differential_array)
    return differential_array
    

def euler_scheme(y0: float, point_x_list: list, func: Function) -> np.ndarray:
    euler_array = init_array(y0, point_x_list)
    for i in range(1, len(euler_array)):
        x = euler_array[i - 1][0]
        y = euler_array[i - 1][1]
        dx = euler_array[i][0] - euler_array[i - 1][0]
        euler_array[i][1] = (y + func.cur_fun(x, y) * dx)
    return euler_array


def improved_euler_scheme(y0: float, point_x_list: list,
                          func: Function) -> np.ndarray:
    euler_array = init_array(y0, point_x_list)

    dx = euler_array[1][0] - euler_array[0][0]
    x_n = euler_array[0][0]

    for i in range(1, len(euler_array)):
        x_n_1 = euler_array[i][0]
        y_n = euler_array[i - 1][1]
        yp = y_n + func.cur_fun(x_n, y_n) * dx
        yc = y_n + func.cur_fun(x_n_1, yp) * dx
        euler_array[i][1] = (yc + yp) / 2
        x_n = x_n_1
    return euler_array


def runge_kutta_4(y0: float, point_x_list: list, func: Function) -> np.ndarray:
    """请确保原函数光滑"""
    runge_kutta_4_array = init_array(y0, point_x_list)
    h = runge_kutta_4_array[1][0] - runge_kutta_4_array[0][0]
    K = np.zeros((5))
    for i in range(1, len(runge_kutta_4_array)):
        xk = runge_kutta_4_array[i - 1][0]
        yk = runge_kutta_4_array[i - 1][1]
        K[1] = func.cur_fun(xk,yk)
        K[2] = func.cur_fun(xk + h / 2, yk + h * K[1] / 2)
        K[3] = func.cur_fun(xk + h / 2, yk + h * K[2] / 2)
        K[4] = func.cur_fun(xk + h, yk + h * K[3])
        K[0] = (K[1] + 2 * K[2] + 2 * K[3] + K[4]) / 6
        yk_1 = yk + K[0] * h
        runge_kutta_4_array[i][1] = yk_1
        # print(K)
    return runge_kutta_4_array


if __name__ == "__main__":
    # y' = y - 2x/y
    # y(0) = 1
    #numpy.around(a, n)
    # a = 0.0
    # b = 1.0
    print("a:")
    a = float(input())
    print("b:")
    b = float(input())
    h = 0.1
    # point_x_list = np.linspace(0.0, 1.0, 11).tolist()
    point_x_list = get_segmented_interval(a,b,h)
    print(np.around(point_x_list, 5))
    y_k = 0
    print("y0:")
    # y0 = 1.0
    y0 = float(input()) 
    func = Function()
    print("euler_scheme")
    print(euler_scheme(y0, point_x_list, func))
    print("improved_euler_scheme")
    print(improved_euler_scheme(y0, point_x_list, func))
    print("runge_kutta_4")
    print(runge_kutta_4(y0, point_x_list, func))