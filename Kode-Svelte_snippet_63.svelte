<script>
      let scriptContent = '';

      async function runScript() {
        const response = await fetch('/api/run_script', {
          method: 'POST',
          body: JSON.stringify({ script: scriptContent })
        });
        // ... håndter respons
      }
    </script>

    <textarea bind:value={scriptContent}></textarea>
    <button on:click={runScript}>Kjør skript</button>