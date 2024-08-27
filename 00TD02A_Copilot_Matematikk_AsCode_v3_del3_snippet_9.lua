-- Store data in Redis
HMSET student:1 cpu_usage 75.5 memory_usage 60.2 network_traffic 500.0 disk_usage 250.0 network_latency 20.5

-- LUA script to calculate percentage utilization
redis.call('HMSET', 'student:1', 'percentage_utilization', (redis.call('HGET', 'student:1', 'cpu_usage') + redis.call('HGET', 'student:1', 'memory_usage')) / 2 * 100)