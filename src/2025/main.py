import day_1 as d1
import day_2 as d2
import day_3 as d3
import day_4 as d4
import day_5 as d5

from utilities import timing_val

@timing_val
def run_stuff():
    print("Day 1")
    d1.solution.main()
    print("Day 2")
    d2.solution.main()
    print("Day 3")
    d3.solution.main()
    print("Day 4")
    d4.solution.main()
    print("Day 5")
    d5.solution.main()
    print("Overall runtime of year 2025")

if __name__ == '__main__':
    run_stuff()
