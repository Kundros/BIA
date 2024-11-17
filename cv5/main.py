from run_all import run_all

from cv5.DifferentialEvolution import DifferentialEvolution

def main():
    run_all(DifferentialEvolution, 100, 10, "3d", 0.5, 0.5)

if __name__ == '__main__':
    main()