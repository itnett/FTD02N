python
import numpy as np

# Probabilities
p_phishing = 0.05       # Probability of a phishing attack
p_malware = 0.01        # Probability of a malware infection
p_ddos = 0.001         # Probability of a DDoS attack

# Impact (hypothetical values)
impact_phishing = 5000  
impact_malware = 10000 
impact_ddos = 20000   

# Calculate expected losses
expected_loss_phishing = p_phishing * impact_phishing
expected_loss_malware = p_malware * impact_malware
expected_loss_ddos = p_ddos * impact_ddos

print(f"Expected loss from phishing: ${expected_loss_phishing}")
print(f"Expected loss from malware: ${expected_loss_malware}")
print(f"Expected loss from DDoS: ${expected_loss_ddos}")