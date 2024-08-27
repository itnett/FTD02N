az sql server create \
    --name mysqlserver<unik> \
    --resource-group MyResourceGroup \
    --location eastus \
    --admin-user sqladmin \
    --admin-password <your_password>

  az sql db create \
    --resource-group MyResourceGroup \
    --server mysqlserver<unik> \
    --name MySQLDB \
    --service-objective S0