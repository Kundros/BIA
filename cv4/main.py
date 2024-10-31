import numpy as np
import multiprocessing as mp

from cv4.GenericAlgorithm import GenericAlgorithm

def calc_path(values):
    points = np.array(values)
    distances = np.linalg.norm(points[1:] - points[:-1], axis=1)
    return np.sum(distances)

def main():
    def GA_10():
        algorithm = GenericAlgorithm(calc_path, -500, 500, 2, "10")
        algorithm.execute(500, 20, 10)
        algorithm.animate_path()

    def GA_20():
        algorithm = GenericAlgorithm(calc_path, -500, 500, 2, "20")
        algorithm.execute(1000, 6, 20)
        algorithm.animate_path()

    def GA_30():
        algorithm = GenericAlgorithm(calc_path, -500, 500, 2, "30")
        algorithm.execute(3000, 20, 30)
        algorithm.animate_path()

    def GA_40():
        algorithm = GenericAlgorithm(calc_path, -500, 500, 2, "40")
        algorithm.execute(800, 100, 40)
        algorithm.animate_path()

    mp.Process(target=GA_10).start()
    mp.Process(target=GA_20).start()
    mp.Process(target=GA_30).start()
    mp.Process(target=GA_40).start()

if __name__ == '__main__':
    main()