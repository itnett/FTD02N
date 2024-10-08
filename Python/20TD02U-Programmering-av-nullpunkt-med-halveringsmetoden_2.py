python
def test_intervals():
    test_cases = [
        (0, 2),      # Gyldig
        (-2, 0),     # Gyldig
        (1, 2),      # Gyldig, høyere nøyaktighet
        (0, 1),      # Ugyldig, samme fortegn
        (-1, 0),     # Ugyldig, samme fortegn
        (3, 2)       # Ugyldig, feil rekkefølge
    ]
    
    for a, b in test_cases:
        try:
            print(f"Testing interval ({a}, {b})")
            root, midpoints = bisection_method(f, a, b)
            print(f"Nullpunktet er x ≈ {root:.4f}\n")
        except ValueError as e:
            print(f"Feil for intervallet ({a}, {b}): {e}\n")

test_intervals()