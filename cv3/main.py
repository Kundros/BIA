from cv3.Annealing import Annealing
from run_all import run_all

def main():
    run_all(Annealing, method_display="heatmap")

if __name__ == '__main__':
    main()