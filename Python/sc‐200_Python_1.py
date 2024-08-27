python
import requests
import json
from collections import Counter

# Function to authenticate with Microsoft Sentinel using Azure AD
def authenticate(client_id, client_secret, tenant_id):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://management.azure.com/.default'
    }
    
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()['access_token']

# Function to fetch incidents from Microsoft Sentinel
def fetch_incidents(access_token, subscription_id, resource_group_name, workspace_name):
    url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/providers/Microsoft.SecurityInsights/incidents?api-version=2020-01-01"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['value']

# Function to analyze incidents
def analyze_incidents(incidents):
    severity_counter = Counter()
    status_counter = Counter()
    tactics_counter = Counter()

    for incident in incidents:
        severity_counter[incident['properties']['severity']] += 1
        status_counter[incident['properties']['status']] += 1
        if 'tactics' in incident['properties']:
            for tactic in incident['properties']['tactics']:
                tactics_counter[tactic] += 1

    return severity_counter, status_counter, tactics_counter

# Example usage
if __name__ == "__main__":
    # Replace these values with your Azure AD and Microsoft Sentinel information
    CLIENT_ID = 'your_client_id'
    CLIENT_SECRET = 'your_client_secret'
    TENANT_ID = 'your_tenant_id'
    SUBSCRIPTION_ID = 'your_subscription_id'
    RESOURCE_GROUP_NAME = 'your_resource_group_name'
    WORKSPACE_NAME = 'your_workspace_name'
    
    # Authenticate with Azure AD
    access_token = authenticate(CLIENT_ID, CLIENT_SECRET, TENANT_ID)
    
    # Fetch incidents from Microsoft Sentinel
    incidents = fetch_incidents(access_token, SUBSCRIPTION_ID, RESOURCE_GROUP_NAME, WORKSPACE_NAME)
    
    # Analyze the incidents
    severity_counts, status_counts, tactics_counts = analyze_incidents(incidents)
    
    # Output results
    print("Incident Severity Counts:")
    for severity, count in severity_counts.items():
        print(f"{severity}: {count}")
    
    print("\nIncident Status Counts:")
    for status, count in status_counts.items():
        print(f"{status}: {count}")
    
    print("\nIncident Tactics Counts:")
    for tactic, count in tactics_counts.items():
        print(f"{tactic}: {count}")