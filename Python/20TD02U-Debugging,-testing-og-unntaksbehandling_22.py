python
import cProfile
import pstats

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# Kjør profilen
profiler = cProfile.Profile()
profiler.enable()
slow_function()
profiler.disable()

# Vis resultatene
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative').print_stats(10)