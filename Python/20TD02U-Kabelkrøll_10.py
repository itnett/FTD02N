python
import math

def beregn_kabelmengde(num_kveiler, d_inner, d_outer):
    d_avg = (d_inner + d_outer) / 2  # cm
    omkrets = math.pi * d_avg  # cm
    total_length_cm = omkrets * num_kveiler  # cm
    total_length_m = total_length_cm / 100  # m
    return total_length_m

def calculate_stift_distance_and_count_adjustable(length, end_distance, max_distance):
    effective_length = length - 2 * end_distance  # cm
    num_intervals = effective_length // max_distance
    ideal_distance = effective_length / (num_intervals + 1)
    num_stifter = num_intervals + 2
    return ideal_distance, num_stifter

def main():
    print("Velkommen til det samlede programmet!")
    print("Velg en av følgende funksjoner:")
    print("1. Beregn kabelmengde")
    print("2. Beregn avstand og antall stifter")

    valg = input("Skriv inn nummeret på funksjonen du vil bruke: ")

    if valg == '1':
        num_kveiler = int(input("Skriv inn antall kveiler på trommelen: "))
        d_inner = float(input("Skriv inn den indre diameteren (i cm): "))
        d_outer = float(input("Skriv inn den ytre diameteren (i cm): "))
        total_length_m = beregn_kabelmengde(num_kveiler, d_inner, d_outer)
        print(f"Total lengde av kabelen på trommelen er ca. {total_length_m:.2f} meter.")
    elif valg == '2':
        length = float(input("Skriv inn lengden på veggen (i cm): "))
        end_distance = float(input("Skriv inn avstanden fra endene til første stift (i cm): "))
        max_distance = float(input("Skriv inn maksimal avstand mellom stiftene (i cm): "))
        ideal_distance, num_stifter = calculate_stift_distance_and_count_adjustable(length, end_distance, max_distance)
        print(f"Den ideelle avstanden mellom stiftene er ca. {ideal_distance:.2f} cm.")
        print(f"Antall stifter langs veggen er {num_stifter}.")
    else:
        print("Ugyldig valg

. Vennligst prøv igjen.")

main()