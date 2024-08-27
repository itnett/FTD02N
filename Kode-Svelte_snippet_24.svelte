<script>
      let currentStep = 1;

      function nextStep() {
        currentStep++;
      }
    </script>

    {#if currentStep === 1}
      <h2>Grunnleggende sikkerhetsprinsipper</h2>
      <p>Lær om konfidensialitet, integritet og tilgjengelighet.</p>
      <button on:click={nextStep}>Neste</button>
    {:else if currentStep === 2}
      <h2>Trusselbilde</h2>
      <p>Bli kjent med vanlige cybertrusler.</p>
      <button on:click={nextStep}>Neste</button>
    {/if}