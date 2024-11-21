import numpy as np

from run_all import run_all

from cv7.SOMA import SOMA

def main():
    run_all(SOMA, 100, 20, "3d", 0.4, 0.11, -0.1, 3)

if __name__ == '__main__':
    main()