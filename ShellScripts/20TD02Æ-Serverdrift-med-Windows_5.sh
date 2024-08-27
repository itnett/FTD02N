bash
    ssh administrator@windows-server "Get-Service | Where-Object {$_.Status -eq 'Running'}"