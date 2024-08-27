az security auto-provisioning-setting update \
    --name default \
    --auto-provision "On"

  az security alert update \
    --name Allow-RDP \
    --enabled true