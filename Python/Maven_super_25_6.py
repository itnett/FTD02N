python
import pdb

def buggy_function(x):
    result = 0
    for i in range(1, x + 1):
        result += i
        if result > 10:  # Breakpoint condition
            pdb.set_trace()  # Start debugging session here
    return result

# Kall funksjonen med en verdi som utløser feil
output = buggy_function(5)
print("Result:", output)