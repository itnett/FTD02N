python
import statistics

data = [2, 4, 4, 4, 5, 5, 7, 9]

gjennomsnitt = statistics.mean(data)      # Output: 5
median = statistics.median(data)         # Output: 4
typetall = statistics.mode(data)          # Output: 4
varians = statistics.variance(data)       # Output: 4
standardavvik = statistics.stdev(data)    # Output: 2