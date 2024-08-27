python
def calculate_stift_distance_and_count_adjustable(length, end_distance, max_distance):
    # Trekke fra avstanden fra endene
    effective_length = length - 2 * end_distance  # cm
    # Finne antall lengder på maksavstanden
    num_intervals = effective_length // max_distance
    # Finne den ideelle avstanden
    ideal_distance = effective_length / (num_intervals + 1)
    # Totalt antall stifter
    num_stifter = num_intervals + 2
    return ideal_distance, num_stifter

def main():
    print("Dette programmet regner ut den ideelle avstanden mellom stiftene og antallet stifter ut fra en gitt lengde.")
    
    length = float(input("Skriv inn lengden på veggen (i cm): "))
    end_distance = float(input("Skriv inn avstanden fra endene til første stift (i cm): "))
    max_distance = float(input("Skriv inn maksimal avstand mellom stiftene (i cm): "))
    
    ideal_distance, num_stifter = calculate_stift_distance_and_count_adjustable(length, end_distance, max_distance)
    
    print(f"Den ideelle avstanden mellom stiftene er ca. {ideal_distance:.2f} cm.")
    print(f"Antall stifter langs veggen er {num_stifter}.")

main()