python
# Decimal to binary
decimal = 42
binary = bin(decimal)
print(f"Decimal {decimal} to binary: {binary}")

# Decimal to hexadecimal
hexadecimal = hex(decimal)
print(f"Decimal {decimal} to hexadecimal: {hexadecimal}")

# Binary to decimal
binary_str = '101010'
decimal_from_binary = int(binary_str, 2)
print(f"Binary {binary_str} to decimal: {decimal_from_binary}")

# Hexadecimal to decimal
hex_str = '2A'
decimal_from_hex = int(hex_str, 16)
print(f"Hexadecimal {hex_str} to decimal: {decimal_from_hex}")