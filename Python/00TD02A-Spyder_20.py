python
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        mindre = [i for i in arr[1:] if i <= pivot]
        større = [i for i in arr[1:] if i > pivot]
        return quicksort(mindre) + [pivot] + quicksort(større)

talliste = [5, 2, 8, 1, 9, 3]
sortert_liste = quicksort(talliste)
print("Sortert liste:", sortert_liste)