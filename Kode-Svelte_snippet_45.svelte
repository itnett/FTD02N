<script>
      let config = '';

      async function saveConfig() {
        const response = await fetch('/api/save_config', {
          method: 'POST',
          body: JSON.stringify({ config })
        });
        // ... håndter respons
      }
    </script>

    <textarea bind:value={config}></textarea>
    <button on:click={saveConfig}>Lagre konfigurasjon</button>