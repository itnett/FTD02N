python
loggoppføring = "2023-06-13 10:22:31 INFO Bruker 'admin' logget inn."
tidspunkt, alvorlighetsgrad, melding = loggoppføring.split(" ", 2)  # Deler opp i tre deler
print(tidspunkt)  # Output: 2023-06-13
print(alvorlighetsgrad)  # Output: 10:22:31
print(melding)  # Output: INFO Bruker 'admin' logget inn.