<script>
  let risks = [
    { name: 'Phishing', likelihood: 'Høy', impact: 'Høy' },
    { name: 'Svak passord', likelihood: 'Middels', impact: 'Middels' },
    // ...
  ];
</script>

<table>
  <tr>
    <th>Risiko</th>
    <th>Sannsynlighet</th>
    <th>Konsekvens</th>
  </tr>
  {#each risks as risk}
    <tr>
      <td>{risk.name}</td>
      <td>{risk.likelihood}</td>
      <td>{risk.impact}</td>
    </tr>
  {/each}
</table>