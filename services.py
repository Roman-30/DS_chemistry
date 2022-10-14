from os import stat

import numpy as np
from scipy.interpolate import UnivariateSpline

from model import *


def read_file(file_path):
    s = stat(file_path)
    if s.st_size >= 1024:
        cur_arr = []
        with open(file_path, "r", encoding="utf8") as f:
            for line in f.readlines()[1:]:
                cur_arr.append([float(x) for x in line.replace(',', '.').split()])
            graph_matrix = np.transpose(cur_arr)
            return Graph(graph_matrix[2], graph_matrix[1])
    else:
        return Graph([], [])


def perform_area_correction(s, graph: GraphModel):
    y_correction = divide_matrix(graph.input.y, s)
    return Graph(graph.input.x, y_correction)


def get_file_name(file_path):
    line = ""
    for i in range(len(file_path) - 1, 0, -1):
        if file_path[i] == '/':
            line = file_path[i + 1: len(file_path)]
            break
    return line


def get_file_type(file_name):
    f_type = ''
    for i in range(len(file_name)):
        if file_name[i] == '.':
            f_type = file_name[i + 1:]
    return f_type


def divide_matrix(arr, s):
    return arr / s


def spline(graph: GraphModel, nodes):
    x = sorted(graph.adjusted.x)
    y = graph.adjusted.y
    spl = UnivariateSpline(x, y, s=nodes)
    spl.set_smoothing_factor(nodes / 100)
    return Graph(np.array(x), np.array(spl(x)))


def find_minimum_positive(arr):
    min_num = 9999
    for i in arr:
        if min_num > i >= 0:
            min_num = i
    return min_num


def find_maximum_negative(arr):
    max_num = -9999
    for i in arr:
        if max_num < i < 0:
            max_num = i
    return max_num


def calculate_E_corrosivity(graph: GraphModel):
    y = graph.spline.y
    a = find_maximum_negative(y)
    b = find_minimum_positive(y)
    i = a if abs(a) < abs(b) else b
    index_e_cor = int(np.where(y == i)[0])
    return graph.spline.x[index_e_cor]


def calculate_final_graph(graph: GraphModel):
    x_final = graph.spline.x - graph.E_cor
    y_final = graph.spline.y * 2.3 * graph.derivative
    return Graph(np.array(x_final), np.array(y_final))


def calculate_point_derivative(graph: GraphModel, interval):
    x = graph.spline.x
    y = graph.spline.y
    left = 99999
    right = 99999
    ind = int(np.where(x == graph.E_cor)[0])
    for i in range(0, len(x)):
        if -1 * interval + x[ind] < x[i] and left == 99999:
            left = i
        elif x[i] > interval + x[ind] and right == 99999:
            right = i
    dl_e = x[right] - x[left]
    dl_i = y[right] - y[left]
    return dl_e / dl_i


def calc_d(e_x, e_y):
    cur_box = []
    num = e_x.shape[0] - 1
    num2 = 1

    x = e_x[num]
    y = e_y[num]

    x2 = e_x[num2]
    y2 = e_y[num2]

    y1_err = abs(y) * 0.99
    y2_err = abs(y2) * 0.99

    for i in range(4, 1001):
        for j in range(4, 1001):
            ans = abs(expression(i / 4, j / 4, x))
            ans2 = abs(expression(i / 4, j / 4, x2))

            if (y1_err < ans < abs(y)) and (
                    y2_err < ans2 < abs(y2)):
                cur_box.append((i / 4, j / 4))
    return cur_box


def calculate_between(m, graph: GraphModel):
    mapa = {}
    for i in m:
        nums = subtract_arrays(m[i], graph.expired.y)
        mapa[i] = sum(nums)
    return mapa


def new_sequence(graph: GraphModel, x):
    ans = {}
    for i in graph.b:
        ans[i] = np.array([expression(i[0], i[1], j) for j in x])
    return ans


def expression(i, j, x):
    return (i * j / (i + j)) * (np.exp(2.3 * x / i) - np.exp(-2.3 * x / j))


def search_index(arr, value):
    num = 999
    ex = 0
    for i in range(len(arr)):
        curr = abs(arr[i] - value)
        if curr < num:
            num = curr
            ex = i
    if num > 1:
        ex = 0
    return ex


def calculate_b(graph: GraphModel):
    return (graph.b_a * graph.b_c) / (2.3 * (graph.b_a + graph.b_c))


def calculate_i_cor(graph: GraphModel):
    return graph.B / graph.derivative * 1000


def calculate_deviation(graph: GraphModel):
    points_deviation = []
    for i in range(len(graph.selection.x)):
        y = graph.expired.y[i]
        y_new = graph.selection.y[i]
        if y_new == 0:
            y_new = 0.1
        points_deviation.append(np.abs(y - y_new) / np.abs(y_new))
    deviation = np.sum(points_deviation) / len(points_deviation) * 100
    return deviation


def subtract_arrays(list_1, list_2):
    result_list = []
    for i in range(len(list_1) - 1):
        result_list.append(abs(list_1[i] - list_2[i]))
    return result_list


def search_min_map_num(lq):
    map_key = ""
    value = 9999
    for i in lq:
        if lq[i] <= value:
            value = lq[i]
            map_key = i
    return map_key
