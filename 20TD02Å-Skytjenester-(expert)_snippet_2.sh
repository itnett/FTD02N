az vm create \
    --resource-group MyResourceGroup \
    --name MyVM \
    --image Win2019Datacenter \
    --admin-username azureuser \
    --admin-password <your_password> \
    --size Standard_D2s_v3