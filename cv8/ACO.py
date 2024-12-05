import collections
from abc import ABC

import numpy as np

from Solution import Solution

class ACO(Solution, ABC):
    def __init__(self, function, lower_bound, upper_bound, dimensions, name):
        super().__init__(function, lower_bound, upper_bound, dimensions, "ACO_" + name)

    def execute(self, generations, cities_number):
        cities = [np.random.uniform(self.lower_bound, self.upper_bound, self.dimensions) for _ in range(cities_number)]

        alpha = 1
        beta = 2
        Q = 1
        ro = 0.5

        self.results = []

        distance_matrix = np.array([
            np.array([np.linalg.norm(np.array([cityA]) - np.array([cityB]), axis=1)[0] for cityB in cities]) for cityA in cities
        ])

        visibility_matrix = np.array([
            np.array([
                (0 if value == 0 else value/(value ** 2)) for value in row
            ]) for row in distance_matrix
        ])

        pheromone_matrix = np.array([
            np.array([
                1.0 for _ in range(cities_number)
            ]) for _ in range(cities_number)
        ])

        glob_best = None

        for _ in range(generations):
            best = None
            best_id = 0
            ant_paths = [[ant_start] for ant_start in range(cities_number)]
            sum_paths = [0 for _ in range(cities_number)]
            for ant_id in range(cities_number):
                for _ in range(cities_number - 1):
                    row_id = ant_paths[ant_id][-1]

                    # Generate individual probabilities before division by sum
                    individuals = np.array([
                        pheromone_matrix[row_id][i] ** alpha *
                        visibility_matrix[row_id][i] ** beta
                        for i in range(cities_number)
                        if i not in ant_paths[ant_id]
                    ])

                    indices = [
                        i for i in range(cities_number)
                        if i not in ant_paths[ant_id]
                    ]

                    # Divide individuals by sum of all to get probability of transitioning
                    summed = individuals.sum()
                    individuals /= summed
                    cumsum_probabilities = np.cumsum(individuals)

                    random_in_range = np.random.uniform()

                    lower_range = 0.

                    for i, x in enumerate(cumsum_probabilities):
                        if lower_range <= random_in_range <= x:
                            ant_paths[ant_id].append(indices[i])
                            sum_paths[ant_id] += distance_matrix[ant_paths[ant_id][-2]][ant_paths[ant_id][-1]]
                            break
                        lower_range = x

                sum_paths[ant_id] += distance_matrix[ant_paths[ant_id][0]][ant_paths[ant_id][-1]]

                if best is None or sum_paths[ant_id] < best:
                    best = sum_paths[ant_id]
                    best_id = ant_id

            # add new best to results
            if glob_best is None or best < glob_best:
                glob_best = best
                self.results.append([cities[i] for i in ant_paths[best_id]])

            # vaporize pheromones
            for i in range(cities_number):
                for j in range(cities_number):
                    pheromone_matrix[i][j] *= (1 - ro)

            # add new pheromones from each ant
            for i, x in enumerate(ant_paths):
                delta_tau = Q / sum_paths[i]
                for k in range(cities_number - 1):
                    pheromone_matrix[x[k]][x[k + 1]] += delta_tau

                pheromone_matrix[x[0]][x[-1]] += delta_tau

    def get_best_in_population(self, population):
        best = self.function(population[0])
        best_index = 0

        for n in range(len(population)):
            new = self.function(population[n])

            if new < best:
                best = new
                best_index = n

        return best, population[best_index]