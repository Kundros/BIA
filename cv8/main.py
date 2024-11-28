import multiprocessing as mp

import numpy as np

from cv8.ACO import ACO

def calc_path(values):
    points = np.array(values)
    distances = np.linalg.norm(points[1:] - points[:-1], axis=1)
    return np.sum(distances)

def main():
    #algorithm = ACO(calc_path, -500, 500, 2, "10")
    #algorithm.execute(100, 10)
    #algorithm.animate_path()
    def GA_10():
        algorithm = ACO(calc_path, -500, 500, 2, "10")
        algorithm.execute(100, 10)
        algorithm.animate_path()

    def GA_20():
        algorithm = ACO(calc_path, -500, 500, 2, "20")
        algorithm.execute(100, 20)
        algorithm.animate_path()

    def GA_30():
        algorithm = ACO(calc_path, -500, 500, 2, "30")
        algorithm.execute(100, 30)
        algorithm.animate_path()

    def GA_40():
        algorithm = ACO(calc_path, -500, 500, 2, "40")
        algorithm.execute(100, 40)
        algorithm.animate_path()

    """def GA_200():
        algorithm = ACO(calc_path, -500, 500, 2, "200")
        algorithm.execute(100, 200)
        algorithm.animate_path()"""

    mp.Process(target=GA_10).start()
    mp.Process(target=GA_20).start()
    mp.Process(target=GA_30).start()
    mp.Process(target=GA_40).start()
    #mp.Process(target=GA_200).start()

if __name__ == '__main__':
    main()