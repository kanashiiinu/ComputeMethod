import numpy as np
import matplotlib.pyplot as plt


class Function:
    def get_ratio(self, x: float) -> float:
        res = self.primitive_function(x) / self.derivative_function(x)
        return res

    def primitive_function(self, x: float):
        res = x * x * x - x - 1
        return res

    def derivative_function(self, x: float):
        res = 3 * x * x - 1
        return res


def newton_iteration(x: float, iteration_num_max: int, downhill_num_max: int,
                     tolerance_error: float, func: Function):
    """[summary]

    Args:
        x ([float]): [初值]
        iteration_num_max ([int]): [迭代最大次数]
        downhill_num_max ([int]): [下山最大次数]
        func ([Function]): [所使用的函数]
        tolerance_error ([float]): [误差限]
    """
    is_downhill = lambda xn_1, xn, func: abs(func.primitive_function(
        xn_1)) < abs(func.primitive_function(xn))
    is_accuracy_enough = lambda xn_1, xn, tolerance_error: abs(
        xn_1 - xn) < tolerance_error
    X = np.zeros((2))
    n = 0
    X[n] = x
    for i in range(iteration_num_max):
        downhill_factor = 1
        ratio = func.get_ratio(X[n])
        X[n + 1] = X[n] - downhill_factor * ratio
        for j in range(downhill_num_max):
            if is_downhill(X[n + 1], X[n], func):
                break
            else:
                downhill_factor /= 2
                X[n + 1] = X[n] - downhill_factor * ratio

        if is_downhill(X[n + 1], X[n], func):
            print("{}\t{}\t{:.8f}".format(i, downhill_factor, X[n + 1]))
        else:
            return "下山失败"
        if is_accuracy_enough(X[n + 1], X[n], tolerance_error):
            return X[n + 1]
        else:
            X[n] = X[n + 1]

    return "超过最大迭代次数"


if __name__ == "__main__":
    x0 = 0.6
    iteration_num_max = 10
    downhill_num_max = 5
    func = Function()
    tolerance_error = 1e-4
    return_val = newton_iteration(x0, iteration_num_max, downhill_num_max,
                                  tolerance_error, func)
    if (type(return_val) is str):
        print(return_val)
    else:
        print(np.around(return_val, 5))
