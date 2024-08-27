python
import hashlib
import random
import string
import json
import time
import matplotlib.pyplot as plt

# --- GRUNNLEGGENDE SIKKERHETSPRINSIPPER ---
def hash_password(password):
    """Genererer en SHA-256 hash av et passord."""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(stored_password_hash, password):
    """Sjekker om et passord matcher den lagrede hash-verdien."""
    return stored_password_hash == hash_password(password)

# --- TRUSSELBILDE INNEN IT-SIKKERHET ---
def simulate_attack(success_rate=0.1):
    """Simulerer et angrep med en gitt suksessrate."""
    return random.random() < success_rate

# --- ANGRPES- OG FORSVARSMETODER ---
def simulate_defense(num_attacks=100, defense_strength=0.5):
    """Simulerer forsvarsmetoder mot flere angrep."""
    successful_attacks = 0
    for _ in range(num_attacks):
        if simulate_attack() and random.random() > defense_strength:
            successful_attacks += 1
    return successful_attacks

# --- RISIKOSTYRING ---
def risk_assessment(threat_likelihood, impact):
    """Utfører en enkel risikovurdering."""
    return threat_likelihood * impact

# --- VISUALISERING AV RISIKOVURDERING ---
def visualize_risk_assessment(risk_levels):
    """Visualiserer risikonivåer."""
    plt.bar(range(len(risk_levels)), risk_levels)
    plt.xlabel('Scenario')
    plt.ylabel('Risikonivå')
    plt.title('Risikovurdering')
    plt.show()

# --- LOVER OG REGLER ---
laws_and_regulations = {
    "GDPR": "General Data Protection Regulation - Beskytter personopplysninger i EU.",
    "NIS": "Network and Information Systems Directive - Forbedrer cybersikkerheten i EU.",
    "CCPA": "California Consumer Privacy Act - Beskytter personopplysninger i California."
}

def find_relevant_laws(keyword):
    """Finner relevante lover og regler basert på et søkeord."""
    return {law: desc for law, desc in laws_and_regulations.items() if keyword.lower() in desc.lower()}

# --- KJØRING AV FUNKSJONER ---
# Grunnleggende sikkerhet: Hashing av passord
password = "sikkerhet123"
hashed_password = hash_password(password)
print(f"Original Password: {password}")
print(f"Hashed Password: {hashed_password}")

# Sjekk passord
password_check = check_password(hashed_password, "sikkerhet123")
print(f"Password check: {'Valid' if password_check else 'Invalid'}")

# Trusselbilde: Simuler angrep
num_simulated_attacks = 1000
successful_attacks = sum(simulate_attack() for _ in range(num_simulated_attacks))
print(f"Number of successful attacks out of {num_simulated_attacks}: {successful_attacks}")

# Angrep- og forsvarsmetoder: Simuler forsvar
defense_strength = 0.7
successful_attacks_after_defense = simulate_defense(num_simulated_attacks, defense_strength)
print(f"Successful attacks after defense: {successful_attacks_after_defense}")

# Risikostyring: Risikovurdering
threat_likelihood = 0.3  # Eksempelverdi
impact = 5  # Eksempelverdi
risk_level = risk_assessment(threat_likelihood, impact)
print(f"Risk level (Likelihood: {threat_likelihood}, Impact: {impact}): {risk_level}")

# Visualisering av risikovurdering
risk_scenarios = [risk_assessment(random.random(), random.randint(1, 10)) for _ in range(10)]
visualize_risk_assessment(risk_scenarios)

# Lover og regler: Finn relevante lover
keyword = "personopplysninger"
relevant_laws = find_relevant_laws(keyword)
print(f"Laws relevant to '{keyword}':")
for law, desc in relevant_laws.items():
    print(f"{law}: {desc}")

# --- LUKK KILDER OG SLUTT ---
print("Skriptet er ferdig.")