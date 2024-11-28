from abc import ABC
import random
from traceback import print_last

import numpy as np
from six import print_

from Solution import Solution

class SOMA(Solution, ABC):
    def __init__(self, function, lower_bound, upper_bound, dimensions, name):
        super().__init__(function, lower_bound, upper_bound, dimensions, "SOMA_" + name)


    ### pop_size >= 2, prt = <0, 1>, step = (0, 1>, min_div = (0, 1>, path_len = (0, 5>
    def execute(self, migrations, pop_size, prt, step, min_div, path_len):
        # create population
        population = np.array([np.random.uniform(self.lower_bound, self.upper_bound, self.dimensions) for _ in range(pop_size)])

        best_val, best_individual = self.get_best_in_population(population)

        self.results = [
            population.copy()
        ]

        # generate all migrations
        for _ in range(migrations):
            # tweak population
            for i, x in enumerate(population):
                t = 0
                local_best = population[i].copy()
                # follow line path by steps
                while t <= path_len:
                    prt_vector = [(1 if np.random.uniform() < prt else 0 )for _ in range(self.dimensions)]
                    # new potential position clipped to borders
                    potent = np.clip(
                        # calculate new position
                        population[i] + (best_individual - population[i]) * t * prt_vector,
                        self.lower_bound, 
                        self.upper_bound
                    )

                    # if potential position is better than local best, update it
                    if self.function(potent) < self.function(local_best):
                        local_best = potent

                    t += step

                # update individual if is better
                if self.function(local_best) < self.function(population[i]):
                    population[i] = local_best

            worst_val, _ = self.get_worst_in_population(population)
            best_val, best_individual = self.get_best_in_population(population)

            self.results.append(
                population.copy()
            )

            if worst_val - best_val < min_div:
                break

    def get_best_in_population(self, population):
        best = self.function(population[0])
        best_index = 0

        for n in range(len(population)):
            new = self.function(population[n])

            if new < best:
                best = new
                best_index = n

        return best, population[best_index]

    def get_worst_in_population(self, population):
        best = self.function(population[0])
        best_index = 0

        for n in range(len(population)):
            new = self.function(population[n])

            if new > best:
                best = new
                best_index = n

        return best, population[best_index]