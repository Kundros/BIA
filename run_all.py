from AlgorithmExecutes import AlgorithmExecutes
import multiprocessing as mp

# Runs search algorithm on all functions, run as separate processes (Warning: uses quite big amount of RAM)
def run_all(algorithm, generations=1000, population=10, method_display="3d"):
    mp.Process(
        target=lambda: AlgorithmExecutes.sphere(algorithm, generations, population, method_display)
    ).start()

    mp.Process(
        target=lambda: AlgorithmExecutes.ashley(algorithm, generations, population, method_display)
    ).start()

    mp.Process(
        target=lambda: AlgorithmExecutes.rastrigin(algorithm, generations, population, method_display)
    ).start()

    mp.Process(
        target=lambda: AlgorithmExecutes.rosenbrock(algorithm, generations, population, method_display)
    ).start()

    mp.Process(
        target=lambda: AlgorithmExecutes.griewank(algorithm, generations, population, method_display)
    ).start()

    mp.Process(
        target=lambda: AlgorithmExecutes.schwefel(algorithm, generations, population, method_display)
    ).start()

    mp.Process(
        target=lambda: AlgorithmExecutes.levy(algorithm, generations, population, method_display)
    ).start()

    mp.Process(
        target=lambda: AlgorithmExecutes.michelewicz(algorithm, generations, population, method_display)
    ).start()

    mp.Process(
        target=lambda: AlgorithmExecutes.zakharow(algorithm, generations, population, method_display)
    ).start()