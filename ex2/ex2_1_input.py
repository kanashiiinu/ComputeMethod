from romberg_algorithm import *


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
