<script>
      import PowerShellScript from './PowerShellScript.svelte';
    </script>

    <PowerShellScript code="Get-Service | Where-Object {$_.Status -eq 'Running'}" />