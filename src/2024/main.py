import day_1 as d1
import day_2 as d2
import day_3 as d3
import day_4 as d4

from utilities import timing_val

@timing_val
def run_stuff():
    d1.solution.main()
    d2.solution.main()
    d3.solution.main()
    d4.solution.main()
    print("Overall runtime of year 2024")

if __name__ == '__main__':
    run_stuff()
