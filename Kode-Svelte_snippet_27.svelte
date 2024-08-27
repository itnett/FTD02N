<script>
      let assets = [];
      let threats = [];
      let vulnerabilities = [];

      // ... funksjoner for å beregne risiko
    </script>

    <form on:submit|preventDefault={calculateRisk}>
      <label for="asset">Verdi:</label>
      <input type="number" id="asset" bind:value={assets[0].value}>

      <label for="threat">Trussel:</label>
      <input type="number" id="threat" bind:value={threats[0].likelihood}>

      <label for="vulnerability">Sårbarhet:</label>
      <input type="number" id="vulnerability" bind:value={vulnerabilities[0].impact}>

      <button type="submit">Beregn risiko</button>
    </form>