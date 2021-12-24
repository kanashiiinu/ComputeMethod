from newton_iteration import *

if __name__ == '__main__':
    print("x0:")
    x0 = float(input())
    print("iteration_num_max:")
    iteration_num_max = int(input())
    print("downhill_num_max:")
    downhill_num_max = int(input())
    func = Function()
    print("tolerance_error:")
    tolerance_error = float(input())
    print("result is :")
    return_val = newton_iteration(x0, iteration_num_max, downhill_num_max,
                                  tolerance_error, func)
    if (type(return_val) is str):
        print(return_val)
    else:
        print(np.around(return_val, 5))
    
    pass
"""
0.6
10
5
1e-4
"""