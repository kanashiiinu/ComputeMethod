from numerical_differentiation import *


class pF(Function):
    def cur_fun(self, x: float, y: float) -> float:
        return self.func_p124_12(x, y)

    def func_p124_12(self, x: float, y: float) -> float:
        """[summary]
        |y' = -y +x +1
        |y(0) = 1
        
        Args:
            x (float): [description]
            y (float): [description]

        Returns:
            float: [description]
        """
        res = -y + x + 1
        return res


if __name__ == "__main__":
    a = 0.0
    b = 2.0
    y0 = 1.0
    func = pF()

    h_euler = 0.1
    point_x_list_euler = get_segmented_interval(a, b, h_euler)
    euler_scheme_arr = euler_scheme(y0, point_x_list_euler, func)
    print(euler_scheme_arr)
    e_x = np.transpose(euler_scheme_arr)[0]
    e_y = np.transpose(euler_scheme_arr)[1]
    plt.subplot(1, 3, 1)
    plt.plot(e_x, e_y, marker='.')
    plt.title("euler")

    h_improved_euler = 0.2
    point_x_list_improved_euler = get_segmented_interval(
        a, b, h_improved_euler)
    improved_euler_arr = improved_euler_scheme(y0, point_x_list_improved_euler,
                                               func)
    print(improved_euler_arr)
    ie_x = np.transpose(improved_euler_arr)[0]
    ie_y = np.transpose(improved_euler_arr)[1]
    plt.subplot(1, 3, 2)
    plt.plot(ie_x, ie_y, marker='.')
    plt.title("euler")

    h_runge_kutta = 0.4
    point_x_list_runge_kutta = get_segmented_interval(a, b, h_runge_kutta)
    runge_kutta_arr = runge_kutta_4(y0, point_x_list_runge_kutta, func)
    print(runge_kutta_arr)
    rt_x = np.transpose(runge_kutta_arr)[0]
    rt_y = np.transpose(runge_kutta_arr)[1]
    plt.subplot(1, 3, 3)
    plt.plot(rt_x, rt_y, marker='.')
    plt.title("runge-kutta")
    plt.show()