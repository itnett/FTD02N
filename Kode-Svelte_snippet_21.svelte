<script>
  let lightOn = false;

  async function toggleLight() {
    const response = await fetch('/api/toggle_light', { method: 'POST' });
    if (response.ok) {
      lightOn = !lightOn;
    }
  }
</script>

<button on:click={toggleLight}>
  {lightOn ? 'Slå av lys' : 'Slå på lys'}
</button>