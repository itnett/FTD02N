az vm create \
    --resource-group MyResourceGroup \
    --name MyLinuxVM \
    --image UbuntuLTS \
    --admin-username azureuser \
    --ssh-key-value ~/.ssh/id_rsa.pub \
    --size Standard_B1s