python
def run_tests():
    all_passed = True
    for task in tasks:
        a, b, c = task["a"], task["b"], task["c"]
        expected_roots = task["expected_roots"]
        if not check_solution(a, b, c, expected_roots):
            print(f"Test failed for equation {a}x^2 + {b}x + {c} = 0. Expected roots: {expected_roots}")
            all_passed = False
        else:
            print(f"Test passed for equation {a}x^2 + {b}x + {c} = 0. Expected roots: {expected_roots}")
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed.")

run_tests()