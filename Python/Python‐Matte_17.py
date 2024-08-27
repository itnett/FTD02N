python
def si_units_examples():
    # Eksempler på SI-enheter og dekadiske prefikser
    length_in_meters = 1.0  # meter
    length_in_kilometers = length_in_meters / 1000  # kilometer
    length_in_millimeters = length_in_meters * 1000  # millimeter
    print(f"Lengde: {length_in_meters} meter, {length_in_kilometers} kilometer, {length_in_millimeters} millimeter")

    mass_in_grams = 1000  # gram
    mass_in_kilograms = mass_in_grams / 1000  # kilogram
    mass_in_milligrams = mass_in_grams * 1000  # milligram
    print(f"Masse: {mass_in_grams} gram, {mass_in_kilograms} kilogram, {mass_in_milligrams} milligram")

    time_in_seconds = 3600  # sekunder
    time_in_hours = time_in_seconds / 3600  # timer
    time_in_minutes = time_in_seconds / 60  # minutter
    print(f"Tid: {time_in_seconds} sekunder, {time_in_hours} timer, {time_in_minutes} minutter")

si_units_examples()