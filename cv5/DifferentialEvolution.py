from abc import ABC
import random
from traceback import print_last

import numpy as np
from six import print_

from Solution import Solution

class DifferentialEvolution(Solution, ABC):
    def __init__(self, function, lower_bound, upper_bound, dimensions, name):
        super().__init__(function, lower_bound, upper_bound, dimensions, "differential_evolution_" + name)

    def execute(self, generations, NP, F, CR):
        # create population
        population = np.array([np.random.uniform(self.lower_bound, self.upper_bound, self.dimensions) for _ in range(NP)])

        edge_ratio = 0.95

        self.results = [
            population
        ]

        for _ in range(generations):
            new_population = population.copy()

            for (i, citizen) in enumerate(new_population):
                while True:
                    r1, r2, r3 = random.sample(range(NP), 3)
                    if r1 != i and r2 != i and r3 != i:
                        break

                x_r1 = new_population[r1]
                x_r2 = new_population[r2]
                x_r3 = new_population[r3]

                v = (x_r1 - x_r2) * F + x_r3

                # If generated normal is out of bounds, move that position to the boundary
                for d in range(len(v)):
                    if v[d] < self.lower_bound * edge_ratio:
                        v[d] = self.lower_bound * edge_ratio
                    elif v[d] > self.upper_bound * edge_ratio:
                        v[d] = self.upper_bound * edge_ratio

                u = np.zeros(self.dimensions)
                j_rnd = np.random.randint(0, self.dimensions)

                for j in range(self.dimensions):
                    if np.random.uniform() < CR or j == j_rnd:
                        u[j] = v[j]
                    else:
                        u[j] = citizen[j]

                f_u = self.function(u)

                if f_u <= self.function(citizen):  # We always accept a solution with the same fitness as a target vector
                    new_population[i] = u

                population = new_population

            self.results.append(population)

        return self.results[-1]