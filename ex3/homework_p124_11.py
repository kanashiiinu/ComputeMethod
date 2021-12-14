from numerical_differentiation import *


class pF(Function):
    def cur_fun(self, x: float, y: float) -> float:
        return self.func_p124_11(x, y)

    def func_p124_11(self, x: float, y: float) -> float:
        """[summary]
        h = 0.2
        求 y(0.4)
        |y' = 8 - 3y
        |y(0) = 2
        
        Args:
            x (float): [description]
            y (float): [description]

        Returns:
            float: [description]
        """
        res = 8 - 3 * y + 0 * x
        return res


if __name__ == "__main__":
    a = 0.0
    b = 0.4
    h = 0.2
    n =  round((b-a)/h) + 1
    point_x_list = np.linspace(a, b, n).tolist()
    print(np.around(point_x_list, 5))
    y0 = 2.0
    func = pF()
    print(runge_kutta_4(y0,point_x_list,func))