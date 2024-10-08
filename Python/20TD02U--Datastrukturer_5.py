python
class Array:
    def __init__(self):
        self.array = []

    def insert(self, item):
        self.array.append(item)

    def remove(self, item):
        self.array.remove(item)

    def linear_search(self, item):
        for i, value in enumerate(self.array):
            if value == item:
                return i
        return -1

    def binary_search(self, item):
        self.array.sort()  # Binary search requires sorted array
        return self._binary_search(item, 0, len(self.array) - 1)

    def _binary_search(self, item, low, high):
        if low <= high:
            mid = (low + high) // 2
            if self.array[mid] == item:
                return mid
            elif self.array[mid] < item:
                return self._binary_search(item, mid + 1, high)
            else:
                return self._binary_search(item, low, mid - 1)
        return -1

    def quick_sort(self):
        self._quick_sort(0, len(self.array) - 1)

    def _quick_sort(self, low, high):
        if low < high:
            pi = self._partition(low, high)
            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)

    def _partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    def display(self):
        return self.array