import functools

import numpy as np

### Contains all functions
class Functions:
    @staticmethod
    def Sphere(parameters):
        return functools.reduce(lambda a, x: a + x ** 2, parameters, 0)

    @staticmethod
    def Ackley(parameters):
        a = 20
        b = 0.2
        c = 2 * np.pi
        d = len(parameters)

        return -a * np.exp(
            -b * np.sqrt( 1 / d * Functions.Sphere(parameters) )
        ) - np.exp(
            1 / d * functools.reduce(lambda a, x: a + np.cos(c * x), parameters, 0)
        ) + a + np.exp(1)

    @staticmethod
    def Rastrigin(parameters):
        d = len(parameters)
        return 10 * d + functools.reduce(lambda a, x: a + (x ** 2 - 10 * np.cos(2 * np.pi * x)), parameters, 0)

    @staticmethod
    def Rosenbrock(parameters):
        sum = 0
        for i in range(len(parameters) - 1):
            sum += 100 * (parameters[i+1] - parameters[i] ** 2) ** 2 + (parameters[i] - 1) ** 2

        return sum

    @staticmethod
    def Griewank(parameters):
        mul = 1
        for i in range(len(parameters)):
            mul *= np.cos(parameters[i] / np.sqrt(i + 1))

        return functools.reduce(lambda a, x: a + (x ** 2) / 4000, parameters, 0) - mul + 1

    @staticmethod
    def Schwefel(parameters):
        d = len(parameters)

        return 418.9829 * d - functools.reduce(lambda a, x: a + x * np.sin(np.sqrt(np.abs(x))), parameters, 0)

    @staticmethod
    def Levy(parameters):
        calc_w = lambda x: 1 + (x - 1)/4

        sum = np.sin(np.pi * calc_w(parameters[0])) ** 2

        for i in range(len(parameters) - 1):
            w = calc_w(parameters[i])
            sum += ((w - 1) ** 2) * (1 + 10 * np.sin(np.pi * w + 1) ** 2)

        wd = calc_w(parameters[-1])

        sum += ((wd - 1) ** 2) * (1 + np.sin(2 * np.pi * wd) ** 2)
        return sum

    @staticmethod
    def Michelewicz(parameters):
        m = 10
        sum = 0

        for i in range(len(parameters)):
            x = parameters[i]
            sum += np.sin(x) * np.sin(((i + 1) * x ** 2) / np.pi) ** (2 * m)

        return - sum

    @staticmethod
    def Zakharow(parameters):
        sum = 0

        for i in range(len(parameters)):
            x = parameters[i]
            sum += 0.5 * (i + 1) * x

        return Functions.Sphere(parameters) + sum ** 2 + sum ** 4