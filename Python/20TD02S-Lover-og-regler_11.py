python
import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from msgraph.core import GraphClient

# Authenticate
credential = DefaultAzureCredential()

# Initialize Azure Resource Management Client
resource_client = ResourceManagementClient(credential, '<your-subscription-id>')

# Initialize GraphClient for Microsoft 365
graph_client = GraphClient(credential=credential)

# Compliance checks for Azure resources
def check_azure_resources():
    compliance_results = {}
    for resource_group in resource_client.resource_groups.list():
        for resource in resource_client.resources.list_by_resource_group(resource_group.name):
            # Placeholder compliance check logic
            compliance_results[resource.id] = "Compliant" if resource.kind != "example-non-compliant-kind" else "Non-compliant"
    return compliance_results

# Compliance checks for Microsoft 365 services
def check_m365_services():
    compliance_results = {}
    users = graph_client.get('/users')
    for user in users.json()['value']:
        # Placeholder compliance check logic
        compliance_results[user['id']] = "Compliant" if 'example-compliant-attribute' in user else "Non-compliant"
    return compliance_results

def main():
    azure_results = check_azure_resources()
    m365_results = check_m365_services()
    results = {
        "Azure": azure_results,
        "M365": m365_results,
    }
    with open("compliance_result.json", "w") as f:
        json.dump(results, f)

if __name__ == "__main__":
    main()