from abc import ABC
import random
from traceback import print_last

import numpy as np
from six import print_

from Solution import Solution

class PSO(Solution, ABC):
    def __init__(self, function, lower_bound, upper_bound, dimensions, name):
        super().__init__(function, lower_bound, upper_bound, dimensions, "PSO_" + name)

    ### v_min and v_max values between 0 and 1 (percentage of whole searchable space)
    def execute(self, M_max, NP, c1, c2, v_min, v_max):
        # create population
        swarm = np.array([np.random.uniform(self.lower_bound, self.upper_bound, self.dimensions) for _ in range(NP)])

        v_min *= self.upper_bound - self.lower_bound
        v_max *= self.upper_bound - self.lower_bound

        edge_ratio = 0.95

        self.results = [
            swarm.copy()
        ]

        v_arr = []
        for i, individual in enumerate(swarm):
            vec = np.random.uniform(v_min, v_max)
            p_x = individual + vec

            v_arr.append(vec)

            # check if individual is not out of function boundaries
            for d in range(len(p_x)):
                if p_x[d] < self.lower_bound * edge_ratio:
                    p_x[d] = self.lower_bound * edge_ratio
                elif p_x[d] > self.upper_bound * edge_ratio:
                    p_x[d] = self.upper_bound * edge_ratio

            swarm[i] = p_x


        g_best = swarm[0].copy()

        for individual in swarm:
            if self.function(individual) < self.function(g_best):
                g_best = individual.copy()

        for m in range(M_max):
            p_best = swarm[0].copy()

            # iterate all individuals in swarm
            for i, x in enumerate(swarm):
                v = self.calc_velocity(v_arr[i], M_max, m, c1, c2, p_best, g_best, x)

                # check the v_min/v_max boundaries for v, and move respectively
                for d in range(len(swarm[i])):
                    if v[d] < v_min[d]:
                        v[d] = v_min[d]
                    elif v[d] > v_max[d]:
                        v[d] = v_max[d]

                initial_x = x.copy()
                swarm[i] += v

                # check if individual is not out of function boundaries
                for d in range(len(swarm[i])):
                    if swarm[i][d] < self.lower_bound * edge_ratio:
                        swarm[i][d] = self.lower_bound * edge_ratio
                    elif swarm[i][d] > self.upper_bound * edge_ratio:
                        swarm[i][d] = self.upper_bound * edge_ratio

                v_arr[i] = swarm[i] - initial_x

                if self.function(swarm[i]) < self.function(p_best):
                    p_best = swarm[i].copy()
                    if self.function(p_best) < self.function(g_best):
                        g_best = p_best.copy()

            self.results.append(swarm.copy())

        return self.results[-1]


    def calc_velocity(self, v, M_max, m, c_1, c_2, p_best, g_best, x):
        w_s = 0.9
        w_e = 0.4

        w = w_s - ( ( (w_s - w_e) * float(m)) / float(M_max) )
        r_1 = np.random.uniform(0, 1)

        return v * w + r_1 * c_1 * (p_best - x) + r_1 * c_2 * (g_best - x)