import os

from numpy import exp
from scipy.interpolate import UnivariateSpline

from model import *


class WindowService:

    def read_file(self, path, graph: GraphModel):
        s = os.stat(path)
        if s.st_size >= 1024:
            cur_arr = []
            with open(path, "r", encoding="utf8") as f:
                for line in f.readlines()[1:]:
                    cur_arr.append([float(x) for x in line.replace(',', '.').split()])
                matrix = np.transpose(cur_arr)
                graph.input = Graph(matrix[2], matrix[1])
        else:
            graph.input = Graph([], [])

    def perform_area_correction(self, s, graph: GraphModel):
        y_correction = self.divide_matrix(graph.input.y, s)
        graph.adjusted = Graph(graph.input.x, y_correction)

    @staticmethod
    def get_file_name(path):
        line = ""
        for i in range(len(path) - 1, 0, -1):
            if path[i] == '/':
                line = path[i + 1: len(path)]
                break
        return line

    @staticmethod
    def divide_matrix(array, s):
        return np.array([float(i / s) for i in array])

    def spline(self, graph: GraphModel, nodes):
        x = sorted(graph.adjusted.x)
        y = graph.adjusted.y
        spl = UnivariateSpline(x, y, s=nodes)
        spl.set_smoothing_factor(nodes / 100)
        graph.spline = Graph(np.array(x), np.array(spl(x)))

    @staticmethod
    def find_minimum_positive(array):
        min_num = 9999
        for i in array:
            if min_num > i >= 0:
                min_num = i
        return min_num

    @staticmethod
    def find_maximum_negative(array):
        max_num = -9999
        for i in array:
            if max_num < i < 0:
                max_num = i
        return max_num

    def calculate_E_corrosivity(self, graph: GraphModel):
        y = graph.spline.y
        a = self.find_maximum_negative(y)
        b = self.find_minimum_positive(y)
        i = a if abs(a) < abs(b) else b
        inf = int(np.where(y == i)[0])
        graph.E_cor = graph.spline.x[inf]

    def calculate_final_graph(self, graph: GraphModel):
        x_final = [i - graph.E_cor for i in graph.spline.x]
        y_final = [i * 2.3 * graph.derivative for i in graph.spline.y]
        graph.expired = Graph(np.array(x_final), np.array(y_final))

    def calculate_point_derivative(self, graph: GraphModel, interval):
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
        graph.derivative = dl_e / dl_i

    def calc_d(self, graph: GraphModel):
        num = int(len(graph.adjusted.x)) - 1
        x = graph.expired.x[num]
        y = graph.expired.y[num]
        for i in range(4, 1001):
            for j in range(4, 1001):
                ans = abs(self.expression(i / 4, j / 4, x))
                if abs(y) * 0.9999 < ans < abs(y):
                    graph.b.append((i / 4, j / 4))
        graph.X_old = x
        graph.Y_old = y

    def calculate_between(self, m, graph: GraphModel):
        mapa = {}
        for i in m:
            nums = self.subtract_arrays(m[i], graph.expired.y)
            mapa[i] = sum(nums)
        return mapa

    def new_sequence(self, graph: GraphModel, x):
        ans = {}
        for i in graph.b:
            ans[i] = [self.expression(i[0], i[1], j) for j in x]
        return ans

    def expression(self, i, j, x):
        return (i * j / (i + j)) * (exp(2.3 * x / i) - exp(-2.3 * x / j))

    @staticmethod
    def search_index(array, value):
        num = 999
        ex = 0
        for i in range(len(array)):
            curr = abs(array[i] - value)
            if curr < num:
                num = curr
                ex = i
        if num > 1:
            ex = 0
        return ex

    def calculate_b(self, graph: GraphModel):
        graph.B = (graph.b_a * graph.b_c) / (2.3 * (graph.b_a + graph.b_c))

    def calculate_i_cor(self, graph: GraphModel):
        graph.I_cor = graph.B / graph.derivative * 1000

    def calculate_deviation(self, graph: GraphModel):
        y_new = self.expression(graph.b_a, graph.b_c, graph.X_old)
        return ((graph.Y_old - y_new) / y_new) * 100

    @staticmethod
    def subtract_arrays(list_1, list_2):
        result_list = []
        for i in range(len(list_1) - 1):
            result_list.append(abs(list_1[i] - list_2[i]))
        return result_list
