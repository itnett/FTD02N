az network nsg create \
    --resource-group MyResourceGroup \
    --name MyNSG

  az network nsg rule create \
    --resource-group MyResourceGroup \
    --nsg-name MyNSG \
    --name Allow-RDP \
    --priority 100 \
    --destination-port-ranges 3389 \
    --protocol Tcp \
    --access Allow \
    --direction Inbound

  az network nic update \
    --resource-group MyResourceGroup \
    --name MyVMNic \
    --network-security-group MyNSG