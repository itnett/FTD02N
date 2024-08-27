<script>
      let risks = [
        { name: 'Forsinket levering', probability: 0.3, impact: 0.8 },
        // ... flere risikoer
      ];

      function calculateRiskScore(risk) {
        return risk.probability * risk.impact;
      }
    </script>

    <table>
      <tr>
        <th>Risiko</th>
        <th>Sannsynlighet</th>
        <th>Konsekvens</th>
        <th>Risikoscore</th>
      </tr>
      {#each risks as risk}
        <tr>
          <td>{risk.name}</td>
          <td>{risk.probability}</td>
          <td>{risk.impact}</td>
          <td>{calculateRiskScore(risk)}</td>
        </tr>
      {/each}
    </table>