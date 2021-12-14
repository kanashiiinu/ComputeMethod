from numerical_differentiation import *

class pF(Function):

    def cur_fun(self, x: float, y: float)->float:
        return super().book_p124_3(x,y)




if __name__=="__main__":
    a = 0.0
    b = 4.0
    point_x_list = np.linspace(a, b, 41).tolist()
    print(np.around(point_x_list, 5))
    y0 = 0
    func = pF()
    print(euler_scheme(y0, point_x_list, func))
    print(improved_euler_scheme(y0, point_x_list, func))
    exact_array = init_array(y0, point_x_list)
    dx = exact_array[1][0] - exact_array[0][0]
    for i in range(0, len(exact_array)):
        x = exact_array[i][0]
        y = exact_array[i][1]
        exact_array[i][1] = x / (1 + x * x)
    print(exact_array)