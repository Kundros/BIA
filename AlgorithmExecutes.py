import numpy as np

from Functions import Functions

# Used for executing individual algorithms and generating corresponding gif
class AlgorithmExecutes:
    @staticmethod
    def sphere(alg, generations = 1000, population = 10, method_display="3d"):
        algorithm = alg(Functions.Sphere, -10, 10, 2, "Sphere")
        algorithm.execute(generations, population)

        if method_display == "3d":
            algorithm.animate_result()
        else:
            algorithm.show_heatmap()

    @staticmethod
    def ashley(alg, generations = 1000, population = 10, method_display="3d"):
        algorithm = alg(Functions.Ackley, -40, 40, 2, "Ackley")
        algorithm.execute(generations, population)

        if method_display == "3d":
            algorithm.animate_result()
        else:
            algorithm.show_heatmap()

    @staticmethod
    def rastrigin(alg, generations = 1000, population = 10, method_display="3d"):
        algorithm = alg(Functions.Rastrigin, -5, 5, 2, "Rastrigin")
        algorithm.execute(generations, population)

        if method_display == "3d":
            algorithm.animate_result()
        else:
            algorithm.show_heatmap()

    @staticmethod
    def rosenbrock(alg, generations = 1000, population = 10, method_display="3d"):
        algorithm = alg(Functions.Rosenbrock, -6, 6, 2, "Rosenbrock")
        algorithm.execute(generations, population)
        if method_display == "3d":
            algorithm.animate_result()
        else:
            algorithm.show_heatmap()

    @staticmethod
    def griewank(alg, generations = 1000, population = 10, method_display="3d"):
        algorithm = alg(Functions.Griewank, -5, 5, 2, "Griewank")
        algorithm.execute(generations, population)

        if method_display == "3d":
            algorithm.animate_result(wired=True)
        else:
            algorithm.show_heatmap()

    @staticmethod
    def schwefel(alg, generations = 1000, population = 10, method_display="3d"):
        algorithm = alg(Functions.Schwefel, -500, 500, 2, "Schwefel")
        algorithm.execute(generations, population)

        if method_display == "3d":
            algorithm.animate_result(wired=True)
        else:
            algorithm.show_heatmap()

    @staticmethod
    def levy(alg, generations = 1000, population = 10, method_display="3d"):
        algorithm = alg(Functions.Levy, -10, 10, 2, "Levy")
        algorithm.execute(generations, population)

        if method_display == "3d":
            algorithm.animate_result()
        else:
            algorithm.show_heatmap()

    @staticmethod
    def michelewicz(alg, generations = 1000, population = 10, method_display="3d"):
        algorithm = alg(Functions.Michelewicz, 0, np.pi, 2, "Michelewicz")
        algorithm.execute(generations, population)

        if method_display == "3d":
            algorithm.animate_result(wired=True)
        else:
            algorithm.show_heatmap()

    @staticmethod
    def zakharow(alg, generations = 1000, population = 10, method_display="3d"):
        algorithm = alg(Functions.Zakharow, -10, 10, 2, "Zakharow")
        algorithm.execute(generations, population)

        if method_display == "3d":
            algorithm.animate_result()
        else:
            algorithm.show_heatmap()