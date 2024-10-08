python
def main():
    # Inform the user about the program
    print("Dette programmet løser likningssettet ax + by = c , dx + ey = f.")
    
    # Get coefficients from the user
    a = float(input("Skriv inn verdien til konstanten a: "))
    b = float(input("Skriv inn verdien til konstanten b: "))
    c = float(input("Skriv inn verdien til konstanten c: "))
    d = float(input("Skriv inn verdien til konstanten d: "))
    e = float(input("Skriv inn verdien til konstanten e: "))
    f = float(input("Skriv inn verdien til konstanten f: "))
    
    # Calculate y
    denominator = (a * e - b * d)
    if denominator == 0:
        print("Likningssettet har ingen unik løsning.")
        return
    
    y = (c * d - a * f) / denominator
    
    # Calculate x
    x = (c - b * y) / a
    
    # Display the solution
    print(f"Løsningen er x = {x}, y = {y}.")

if __name__ == "__main__":
    main()