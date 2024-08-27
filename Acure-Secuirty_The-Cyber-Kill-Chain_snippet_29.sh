# Log in to Azure
az login

# List all subscriptions
az account list

# List all resource groups
az group list

# List all resources in a specific resource group
az resource list --resource-group example-resource-group

# List virtual machines and their details
az vm list --output table