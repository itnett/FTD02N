az sentinel create \
    --resource-group MyResourceGroup \
    --workspace-name MyLogAnalyticsWorkspace

  az sentinel data-source connect \
    --resource-group MyResourceGroup \
    --workspace-name MyLogAnalyticsWorkspace \
    --data-source AzureActivity

  az sentinel data-source connect \
    --resource-group MyResourceGroup \
    --workspace-name MyLogAnalyticsWorkspace \
    --data-source AzureSecurityCenter