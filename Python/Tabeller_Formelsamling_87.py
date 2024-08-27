python
# Eksempel: Boblesortering

def boblesortering(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Bruk av boblesortering
arr = [64, 34, 25, 12, 22, 11, 90]
boblesortering(arr)
print("Sortert array:", arr)