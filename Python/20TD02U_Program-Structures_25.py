python
def switch_case(value):
    return {
        'case1': "Result for case 1",
        'case2': "Result for case 2",
    }.get(value, "Default case")

print(switch_case('case1'))  # Output: Result for case 1