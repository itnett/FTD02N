python
nested_list = [[1, 2], [3, 4]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4]