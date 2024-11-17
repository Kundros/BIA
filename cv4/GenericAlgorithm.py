from abc import ABC

import numpy
import numpy as np

from Solution import Solution

class GenericAlgorithm(Solution, ABC):
    def __init__(self, function, lower_bound, upper_bound, dimensions, name):
        super().__init__(function, lower_bound, upper_bound, dimensions, "generic_algorithm_" + name)

    def execute(self, generations, NP, D):
        cities = np.array([np.random.uniform(self.lower_bound, self.upper_bound, self.dimensions) for _ in range(D)])

        # create population
        population = []

        for _ in range(NP):
            copied_cities = cities.copy()
            np.random.shuffle(copied_cities)
            population.append(copied_cities)

        (best, res) = self.get_best_in_population(population)

        self.results = [
            res
        ]

        for _ in range(generations):
            new_population = population.copy()

            for j in range(NP):
                # set parent_A from the current index
                parent_A = population[j]

                # select random parent_B where parent_B != parent_A
                while True:
                    i = np.random.randint(0, NP)
                    if i != j:
                        parent_B = population[i]
                        break

                # generate first half of the offspring
                first_half = parent_A[0:int(len(parent_A)/2)]
                # prepare second half for the other offspring part
                second_half = []

                sum_false = 0
                # create offspring
                for city in parent_B:
                    if not numpy.isin(city, first_half).all():
                        sum_false += 1
                        second_half.append(city)

                offspring_AB = numpy.concatenate((first_half, np.array(second_half)))

                # try mutate
                if np.random.uniform() < .6:
                    mut_1 = np.random.randint(0, D)
                    while True:
                        mut_2 = np.random.randint(0, D)
                        if mut_1 != mut_2:
                            break

                    temp = offspring_AB[mut_2].copy()
                    offspring_AB[mut_2] = offspring_AB[mut_1]
                    offspring_AB[mut_1] = temp

                # evaluate on offspring
                new = self.function(offspring_AB)
                if new < best:
                    best = new
                    self.results.append(offspring_AB)

                if self.function(offspring_AB) < self.function(parent_A):
                    new_population[j] = offspring_AB

            population = new_population

        return self.results[-1]

    def get_best_in_population(self, population):
        best = self.function(population[0])
        best_index = 0

        for n in range(len(population)):
            new = self.function(population[n])

            if new < best:
                best = new
                best_index = n

        return best, population[best_index]