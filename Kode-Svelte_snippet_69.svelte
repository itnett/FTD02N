<script>
      let logFile = '';
      let analysisResults = '';

      async function analyzeLog() {
        const response = await fetch('/api/analyze_log', {
          method: 'POST',
          body: JSON.stringify({ logFile })
        });
        analysisResults = await response.text();
      }
    </script>

    <input type="file" bind:files={logFile} />
    <button on:click={analyzeLog}>Analyser logg</button>
    <pre>{analysisResults}</pre>