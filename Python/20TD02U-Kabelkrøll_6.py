python
def calculate_stift_distance(length, end_distance, max_distance):
    # Trekke fra avstanden fra endene
    effective_length = length - 2 * end_distance  # cm
    # Finne antall lengder på maksavstanden
    num_intervals = effective_length // max_distance
    # Finne den ideelle avstanden
    ideal_distance = effective_length / (num_intervals + 1)
    return ideal_distance

length = 300  # cm
end_distance = 5  # cm
max_distance = 20  # cm

ideal_distance = calculate_stift_distance(length, end_distance, max_distance)
print(f"Den ideelle avstanden mellom stiftene er ca. {ideal_distance:.2f} cm.")