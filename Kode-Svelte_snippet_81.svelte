<script>
      import IaCCodeBlock from './IaCCodeBlock.svelte';
    </script>

    <IaCCodeBlock language="terraform">
      resource "azurerm_resource_group" "example" {
        name     = "example-resources"
        location = "West Europe"
      }
    </IaCCodeBlock>