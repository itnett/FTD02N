python
import time
import random

# Simulering av dataoverføring
def simulate_data_transfer():
    data_size = random.randint(500, 1500)  # i kilobytes
    transfer_time = random.uniform(0.5, 2)  # i sekunder
    throughput = data_size / transfer_time  # i KB/s
    return throughput

# Mål ytelsen over flere overføringer
num_transfers = 10
throughputs = []

for _ in range(num_transfers):
    throughput = simulate_data_transfer()
    throughputs.append(throughput)
    print(f"Overføring gjennomstrømning: {throughput:.2f} KB/s")
    time.sleep(1)

# Beregn gjennomsnittlig gjennomstrømning
average_throughput = sum(throughputs) / len(throughputs)
print(f"\nGjennomsnittlig nettverksytelse: {average_throughput:.2f} KB/s")