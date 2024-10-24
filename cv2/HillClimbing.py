import random
from abc import ABC

import numpy as np

from Solution import Solution

class HillClimbing(Solution, ABC):
    def __init__(self, function, lower_bound, upper_bound, dimensions, name):
        super().__init__(function, lower_bound, upper_bound, dimensions, "hill_climbing_" + name)

    def execute(self, generations, population):
        # create sigma as 20% of whole range
        sigma = (self.upper_bound - self.lower_bound) * .2

        # create first random point
        self.results = [
            [
                random.uniform(self.lower_bound, self.upper_bound) for _ in range(self.dimensions)
            ]
        ]

        x_b_value = self.function(self.results[0])

        # Generate all generations
        for _ in range(generations):
            x_s_value = float("inf")
            x_s = None

            # Make population and select the best one
            for n in range(population):
                # generate one random normal
                np_n = np.random.normal(self.results[-1], sigma)

                # If generated normal is out of bounds, move that position to the boundary
                for d in range(len(np_n)):
                    if np_n[d] < self.lower_bound:
                        np_n[d] = self.lower_bound
                    if np_n[d] > self.upper_bound:
                        np_n[d] = self.upper_bound

                np_value = self.function(np_n)

                # check if is best in the population
                if np_value < x_s_value:
                    x_s_value = np_value
                    x_s = np_n

            # if population representation is better than current best, then update it
            if x_s_value < x_b_value:
                x_b_value = x_s_value
                self.results.append(x_s)

        return self.results[-1]