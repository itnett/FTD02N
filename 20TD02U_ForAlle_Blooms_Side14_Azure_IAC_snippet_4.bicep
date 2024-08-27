module vnet 'vnet.bicep' = {
  name: 'vnetModule'
  params: {
    location: resourceGroup().location
    vnetName: 'myVNet'
  }
}