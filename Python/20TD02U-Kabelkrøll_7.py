python
def calculate_num_stifter(length, end_distance, max_distance):
    # Trekke fra avstanden fra endene
    effective_length = length - 2 * end_distance  # cm
    # Finne antall lengder på maksavstanden
    num_intervals = effective_length // max_distance
    # Totalt antall stifter
    num_stifter = num_intervals + 2
    return num_stifter

num_stifter = calculate_num_stifter(length, end_distance, max_distance)
print(f"Antall stifter langs veggen er {num_stifter}.")