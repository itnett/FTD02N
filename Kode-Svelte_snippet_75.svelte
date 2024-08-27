<script>
      let currentStep = 'Hendelse registreres';
      let incidentStatus = 'Åpen';

      function handleIncident() {
        // ... logikk for å håndtere hendelsen
        incidentStatus = 'Løst';
      }
    </script>

    <p>Nåværende steg: {currentStep}</p>
    <p>Hendelsestatus: {incidentStatus}</p>
    <button on:click={handleIncident}>Håndter hendelse</button>