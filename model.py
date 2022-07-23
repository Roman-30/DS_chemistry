import numpy as np


class GraphModel:

    def __init__(self):
        self.input = None
        self.adjusted = None
        self.spline = None
        self.expired = None
        self.E_cor = 0
        self.derivative = 0
        self.b = []
        self.b_a = 0
        self.b_c = 0
        self.B = 0
        self.X_old = 0
        self.Y_old = 0
        self.I_cor = 0


class Graph:

    def __init__(self, x, y):
        self.x = x
        self.y = y
