provider "azurerm" {
     features {}
   }

   resource "azurerm_resource_group" "rg" {
     name     = "myResourceGroup"
     location = "West Europe"
   }

   resource "azurerm_virtual_network" "vnet" {
     name                = "myVnet"
     address_space       = ["10.0.0.0/16"]
     location            = azurerm_resource_group.rg.location
     resource_group_name = azurerm_resource_group.rg.name
   }

   resource "azurerm_subnet" "subnet" {
     name                 = "mySubnet"
     resource_group_name  = azurerm_resource_group.rg.name
     virtual_network_name = azurerm_virtual_network.vnet.name
     address_prefixes     = ["10.0.1.0/24"]
   }

   resource "azurerm_network_interface" "nic" {
     name                = "myNIC"
     location            = azurerm_resource_group.rg.location
     resource_group_name = azurerm_resource_group.rg.name

     ip_configuration {
       name                          = "internal"
       subnet_id                     = azurerm_subnet.subnet.id
       private_ip_address_allocation = "Dynamic"
     }
   }

   resource "azurerm_linux_virtual_machine" "vm" {
     name                = "myVM"
     resource_group_name = azurerm_resource_group.rg.name
     location            = azurerm_resource_group.rg.location
     size                = "Standard_DS1_v2"
     admin_username      = "adminuser"
     network_interface_ids = [
       azurerm_network_interface.nic.id,
     ]

     admin_ssh_key {
       username   = "adminuser"
       public_key = file("~/.ssh/id_rsa.pub")
     }

     os_disk {
       caching              = "ReadWrite"
       storage_account_type = "Standard_LRS"
     }

     source_image_reference {
       publisher = "Canonical"
       offer     = "UbuntuServer"
       sku       = "18.04-LTS"
       version   = "latest"
     }
   }