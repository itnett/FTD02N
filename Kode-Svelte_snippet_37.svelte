<script>
      let sqlQuery = '';
      let queryResult = '';

      async function executeQuery() {
        const response = await fetch('/api/execute_sql', {
          method: 'POST',
          body: JSON.stringify({ query: sqlQuery })
        });
        queryResult = await response.text();
      }
    </script>

    <textarea bind:value={sqlQuery}></textarea>
    <button on:click={executeQuery}>Kjør spørring</button>
    <pre>{queryResult}</pre>