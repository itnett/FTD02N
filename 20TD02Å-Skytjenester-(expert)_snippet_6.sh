az backup vault create \
    --resource-group MyResourceGroup \
    --name MyRecoveryServicesVault \
    --location eastus

  az backup protection enable-for-vm \
    --resource-group MyResourceGroup \
    --vault-name MyRecoveryServicesVault \
    --vm MyVM \
    --policy-name DefaultPolicy