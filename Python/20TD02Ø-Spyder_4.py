python
    def simulate_distribution(distro_name):
        client = docker.from_env()
        container = client.containers.run(f"{distro_name}:latest", command="/bin/bash", detach=True, tty=True)
        # Kjør kommandoer inne i containeren for å demonstrere forskjeller
        # ...
        container.stop()