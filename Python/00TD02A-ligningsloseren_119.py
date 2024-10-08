python
def check_solution(a, b, c, expected_roots):
    actual_roots = solve_quadratic(a, b, c)
    actual_roots = {round(root.real, 2) for root in actual_roots}  # Ignorerer imaginære deler hvis de er null
    expected_roots = {round(root, 2) for root in expected_roots}
    return actual_roots == expected_roots