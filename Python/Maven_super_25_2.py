python
def fibonacci(n):
    if n <= 0:
        return "Input må være et positivt heltall"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print de første 10 Fibonacci-tallene
for i in range(1, 11):
    print(fibonacci(i))