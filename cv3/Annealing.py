import random
from abc import ABC

import numpy as np

from Solution import Solution

class Annealing(Solution, ABC):
    def __init__(self, function, lower_bound, upper_bound, dimensions, name):
        super().__init__(function, lower_bound, upper_bound, dimensions, "annealing_" + name)

    def execute(self, generations, population):
        # annealing parameters
        T = 100
        T_min = 0.005
        alpha = 0.93

        # create sigma as 20% of whole range
        sigma = (self.upper_bound - self.lower_bound) * .2
        edge_ratio = 0.95

        # create first random point
        self.results = [
            np.random.uniform(self.lower_bound, self.upper_bound, self.dimensions)
        ]

        # Simulate annealing
        while T > T_min:
            x_1 = np.random.normal(self.results[-1], sigma)

            # If generated normal is out of bounds, move that position to the boundary
            for d in range(len(x_1)):
                if x_1[d] < self.lower_bound * edge_ratio:
                    x_1[d] = self.lower_bound * edge_ratio
                if x_1[d] > self.upper_bound * edge_ratio:
                    x_1[d] = self.upper_bound * edge_ratio

            f_x = self.function(self.results[-1])
            f_x_1 = self.function(x_1)

            energy_variation = f_x_1-f_x

            if energy_variation < 0:
                self.results.append(x_1)
            else:
                r = np.random.uniform(0, 1)

                if r < (np.e ** (-energy_variation/T)):
                    self.results.append(x_1)

            T *= alpha

        return self.results[-1]