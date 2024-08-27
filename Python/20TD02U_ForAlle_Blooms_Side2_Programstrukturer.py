python
def quicksort(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[0]
    mindre = [x for x in liste[1:] if x <= pivot]
    større = [x for x in liste[1:] if x > pivot]
    return quicksort(mindre) + [pivot] + quicksort(større)