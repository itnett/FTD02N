python
def solve_linear_equations(a, b, c, d, e, f):
    """
    Solve the system of linear equations:
    ax + by = c
    dx + ey = f
    """
    # Check if the equations have a unique solution
    determinant = a * e - b * d
    if determinant == 0:
        return "The system has no unique solution."

    # Solve for y
    y = (c * d - a * f) / determinant

    # Solve for x using the value of y
    x = (c - b * y) / a

    return x, y

def main():
    print("This program solves a system of linear equations of the form:")
    print("ax + by = c")
    print("dx + ey = f")
    
    # Get coefficients from the user
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter constant c: "))
    d = float(input("Enter coefficient d: "))
    e = float(input("Enter coefficient e: "))
    f = float(input("Enter constant f: "))
    
    solution = solve_linear_equations(a, b, c, d, e, f)
    
    if isinstance(solution, str):
        print(solution)
    else:
        x, y = solution
        print(f"The solution is x = {x}, y = {y}")

if __name__ == "__main__":
    main()