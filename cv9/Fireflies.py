from abc import ABC

import numpy as np

from Solution import Solution


class Fireflies(Solution, ABC):
    def __init__(self, function, lower_bound, upper_bound, dimensions, name):
        super().__init__(function, lower_bound, upper_bound, dimensions, "ACO_" + name)

    def execute(self, generations, pop_size):
        # create all fireflies
        fireflies = [np.random.uniform(self.lower_bound, self.upper_bound, self.dimensions) for _ in range(pop_size)]

        beta_0 = 1
        alpha = 0.3

        self.results = [fireflies]

        # iterate all generations
        for _ in range(generations):
            # all fireflies
            for i in range(pop_size):
                # for current firefly, calculate if it should move towards other firefly
                for j in range(pop_size):
                    # negative function because we're looking for global minima,
                    # so lower the number the better
                    light_i = -self.function(fireflies[i])
                    light_j = -self.function(fireflies[j])

                    # check if light of the other firefly is better
                    if light_j > light_i:
                        r = np.linalg.norm(np.array(fireflies[i]) - np.array(fireflies[j]))
                        beta = beta_0 / (1 + r)
                        # move towards the other firefly
                        fireflies[i] += beta * (fireflies[j] - fireflies[i]) + alpha * (np.random.rand(self.dimensions) - 0.5)
                        fireflies[i] = np.clip(fireflies[i], self.lower_bound, self.upper_bound)

            self.results.append(fireflies.copy())