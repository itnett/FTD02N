python
import heapq

class Patient:
    def __init__(self, name, priority, arrival_time):
        self.name = name
        self.priority = priority
        self.arrival_time = arrival_time

    def __lt__(self, other):  # For comparison in the priority queue
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority > other.priority

class PriorityQueueWithAging:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient):
        heapq.heappush(self.queue, patient)

    def dequeue(self):
        patient = heapq.heappop(self.queue)
        return patient

    def age_patients(self, time_increment):
        for patient in self.queue:
            # Increase priority based on time waited and initial priority
            patient.priority += time_increment * (4 - patient.priority)  # Example aging formula