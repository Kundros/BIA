import numpy as np

from run_all import run_all

from cv6.PSO import PSO

def main():
    run_all(PSO, 50, 15, "3d", 2.0, 2.0, np.array([-0.03, -0.03]), np.array([0.03, 0.03]))

if __name__ == '__main__':
    main()