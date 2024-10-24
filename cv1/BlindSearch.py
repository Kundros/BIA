import random
from abc import ABC

from Solution import Solution

class BlindSearch(Solution, ABC):
    def __init__(self, function, lower_bound, upper_bound, dimensions, name):
        super().__init__(function, lower_bound, upper_bound, dimensions, "blind_search_" + name)

    def execute(self, generations, population):
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
                # create one random point
                np_n = [
                    random.uniform(self.lower_bound, self.upper_bound) for _ in range(self.dimensions)
                ]

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
