import day_1 as d1
import day_2 as d2
from utilities import timing_val

@timing_val
def run_stuff():
    d1.solution.main()
    d2.solution.main()
    print("Overall runtime of year 2024.")

if __name__ == '__main__':
    run_stuff()
