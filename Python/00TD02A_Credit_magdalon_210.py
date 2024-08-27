python
   import random

   def simulate_response_time(mean, std_dev):
       """Simulate response time based on normal distribution."""
       response_time = random.gauss(mean, std_dev)
       return max(0, response_time)  # Ensure non-negative response time

   mean_response_time = 50  # ms
   std_dev_response_time = 10  # ms

   response_times = [simulate_response_time(mean_response_time, std_dev_response_time) for _ in range(1000)]
   print("Simulated response times:", response_times[:10])