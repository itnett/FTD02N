python
def test_intervals():
    test_cases = [
        (0, 2),      # gyldig
        (-2, 0),     # gyldig
        (1, 2),      # gyldig, høyere nøyaktighet
        (0, 1),      # ugyldig, samme fortegn
        (-1, 0),     # ugyldig, samme fortegn
        (3, 2)       # ugyldig, feil rekkefølge
    ]
    
    for a, b in test_cases:
        try:
            print(f"testing interval ({a}, {b})")
            root, midpoints = bisection_method(f, a, b)
            print(f"nullpunktet er x ≈ {root:.4f}\n")
        except ValueError as e:
            print(f"feil for intervallet ({a}, {b}): {e}\n")

test_intervals()