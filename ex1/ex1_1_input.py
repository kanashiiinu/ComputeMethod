from interpolation_fitting import *

if __name__ == "__main__":
    a = -5
    b = 5
    print("input inter_point num:")
    n = int(input())
    inter_point_x_list = np.linspace(a, b, n)
    inter_point_list = [inter_point_x_list,inter_point_x_list]
    inter_point_list = np.transpose(np.array(inter_point_list))
    for point in inter_point_list:
        point[1] = 1 / (1 + point[0] * point[0])
        pass
    print("input inter_value:")
    input_num = float(input())
    print("accurate val:")
    accurate_val = 1/(1+input_num*input_num) 
    print(accurate_val)
    print("拉格良日插值")
    val_l = lagrange_interpolation(inter_point_list, input_num)
    print(val_l)
    print("分段线性插值")
    val_p = piecewise_lagrange_interpolation(inter_point_list, input_num)
    print(val_p)
    print("误差（拉）:")
    print(accurate_val-val_l)
    print("误差（分）")
    print(accurate_val-val_p)
    
