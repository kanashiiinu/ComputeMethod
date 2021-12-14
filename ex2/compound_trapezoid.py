import numpy as np
import matplotlib.pyplot as plt



def compound_trapezoid(inter_point_list: list) -> float:
    inter_point_array = np.transpose(np.array(inter_point_list))
    n = len(inter_point_array)
    T = 0
    for i in range(n - 1):
        s = (inter_point_array[i][1] + inter_point_array[i + 1][1]) / 2
        h = inter_point_array[i + 1][0] - inter_point_array[i][0]
        T += s * h
    return T


if __name__ == "__main__":
    
    inter_point_3_list = [[], [], []]
    read_line = "x 7.0 10.5 13.0 17.5 34.0 40.5 44.5 48.0 56.0".split(" ")[1:]
    inter_point_3_list[0].extend((list(map(float, read_line))))
    read_line = "y1 44 45 47 50 50 38 30 30 34".split(" ")[1:]
    inter_point_3_list[1].extend(list(map(float, read_line)))
    read_line = "y2 44 59 70 72 93 100 110 110 110".split(" ")[1:]
    inter_point_3_list[2].extend(list(map(float, read_line)))
    read_line = "x 111.5 118.0 123.5 136.5 142.0 146.0 150.0 157.0 158.0".split(
        " ")[1:]
    inter_point_3_list[0].extend(list(map(float, read_line)))
    read_line = "y1 32 65 55 54 52 50 66 66 68".split(" ")[1:]
    inter_point_3_list[1].extend(list(map(float, read_line)))
    read_line = "y2 121 122 116 83 81 82 86 85 68".split(" ")[1:]
    inter_point_3_list[2].extend(list(map(float, read_line)))

    down_list = inter_point_3_list[0:2]
    up_list = inter_point_3_list[::2]

    land_s = (compound_trapezoid(up_list) \
            - compound_trapezoid(down_list)) \
            * ((40 / 18) \
            * (40 / 18))
    print(np.around(land_s,2))
    exact_val = 41288
    error_val = abs(land_s - exact_val)
    print("{:.2%}".format(error_val/exact_val))
