<script>
      let ipAddress = '';

      async function ping() {
        const response = await fetch(`/api/ping?ipAddress=${ipAddress}`);
        // ... håndter respons og vis resultat
      }
    </script>

    <input type="text" bind:value={ipAddress} placeholder="IP-adresse">
    <button on:click={ping}>Ping</button>