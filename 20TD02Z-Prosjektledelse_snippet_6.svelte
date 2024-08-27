<script>
      // ... hent data fra API
      let risks = [/* ... */];
    </script>

    <table>
      <tr>
        <th>Risiko</th>
        <th>Sannsynlighet</th>
        <th>Konsekvens</th>
        <th>Tiltak</th>
      </tr>
      {#each risks as risk}
        <tr>
          <td>{risk.name}</td>
          <td>{risk.probability}</td>
          <td>{risk.impact}</td>
          <td>{risk.mitigation}</td>
        </tr>
      {/each}
    </table>