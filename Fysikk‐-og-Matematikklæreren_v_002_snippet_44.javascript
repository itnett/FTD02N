function generateCodeForTrinket(topic, input) {
    let code = "";

    switch (topic) {
        case "regneregler":
            const num1 = input.num1;
            const operator = input.operator;
            const num2 = input.num2;
            code = `
# Python code for basic arithmetic operations
num1 = ${num1}
num2 = ${num2}
operator = '${operator}'

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")

if 'result' in locals():
    print(f"{num1} {operator} {num2} = {result}")
`;
            break;
        case "pythagoras":
            const a = input.katet1 || input.knownKatet;
            const b = input.katet2 || input.knownKatet;
            const c = input.hypotenuse;
            if (input.pythagorasOption === "hypotenuse") {
                code = `
# Python code for Pythagorean theorem (finding hypotenuse)
import math

a = ${a}
b = ${b}

c = math.sqrt(a**2 + b**2)
print(f"The hypotenuse (c) is: {c:.2f}")
`;
            } else {
                code = `
# Python code for Pythagorean theorem (finding leg)
import math

c = ${c}
known_katet = ${knownKatet}

unknown_katet = math.sqrt(c**2 - known_katet**2)
print(f"The unknown leg is: {unknown_katet:.2f}")
`;
            }
            break;
        // Add cases for other topics as needed
    }

    return code;
}

// Implement similar functions for generating GeoGebra and Casio fx-991CW code