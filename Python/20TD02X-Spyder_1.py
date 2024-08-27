python
import random
import pandas as pd
import matplotlib.pyplot as plt

# --- MONITORERING OG STRATEGI FOR OVERVÅKING ---
def monitor_system(activity_log):
    """Simulerer overvåking av et system ved å generere en aktivitetslogg."""
    activities = ['login', 'logout', 'file_access', 'file_modification', 'network_request']
    log = []
    for _ in range(activity_log):
        activity = random.choice(activities)
        timestamp = pd.Timestamp.now()
        log.append({'timestamp': timestamp, 'activity': activity})
    return log

def identify_security_breach(log):
    """Identifiserer potensielle sikkerhetsbrudd basert på aktivitetsloggen."""
    breaches = [entry for entry in log if entry['activity'] == 'file_modification']
    return breaches

# --- VERKTØY FOR OVERVÅKING OG PRESENTASJON AV RESULTATER ---
def present_results(log, breaches):
    """Presenterer aktivitetsloggen og sikkerhetsbrudd visuelt."""
    df = pd.DataFrame(log)
    breach_df = pd.DataFrame(breaches)
    
    print("Aktivitetslogg:")
    print(df)
    
    print("\nIdentifiserte sikkerhetsbrudd:")
    print(breach_df)
    
    plt.figure(figsize=(10, 6))
    df['activity'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Aktivitetsfordeling')
    plt.xlabel('Aktivitet')
    plt.ylabel('Antall')
    plt.show()
    
    if not breach_df.empty:
        plt.figure(figsize=(10, 6))
        breach_df['timestamp'].value_counts().plot(kind='bar', color='salmon')
        plt.title('Tidspunkter for sikkerhetsbrudd')
        plt.xlabel('Tidspunkt')
        plt.ylabel('Antall')
        plt.show()

# --- DIGITAL ETTERFORSKNING ---
def perform_digital_forensics(log):
    """Utfører en enkel digital etterforskning ved å analysere loggdata."""
    file_access_log = [entry for entry in log if entry['activity'] == 'file_access']
    return file_access_log

# --- IDS/IPS EKSEMPEL ---
def ids_simulation(log):
    """Simulerer et Intrusion Detection System (IDS) som identifiserer mistenkelige aktiviteter."""
    ids_alerts = [entry for entry in log if entry['activity'] == 'network_request']
    return ids_alerts

# --- VERKTØY FOR SIKKERHETSANALYSE OG TILTAKSANALYSE ---
def security_analysis(log):
    """Utfører en enkel sikkerhetsanalyse og anbefaler tiltak."""
    breaches = identify_security_breach(log)
    if breaches:
        print("Tiltak: Vurder å begrense filtilgang og øke overvåkingsnivået.")
    else:
        print("Ingen sikkerhetsbrudd identifisert.")

# --- HOVEDFUNKSJON FOR Å KJØRE EKSEMPLENE ---
def run_monitoring_and_forensics():
    print("Starter monitorering og digital etterforskning...")
    activity_log = 100
    log = monitor_system(activity_log)
    breaches = identify_security_breach(log)
    present_results(log, breaches)
    
    forensics_log = perform_digital_forensics(log)
    print("\nDigital etterforskning - filtilgangslogg:")
    print(pd.DataFrame(forensics_log))
    
    ids_alerts = ids_simulation(log)
    print("\nIDS Alert logg:")
    print(pd.DataFrame(ids_alerts))
    
    security_analysis(log)
    print("Monitorering og digital etterforskning fullført.")

run_monitoring_and_forensics()