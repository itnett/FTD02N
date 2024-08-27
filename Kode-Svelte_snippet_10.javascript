// Svelte-komponent
<script>
  async function runPlaybook(playbookName) {
    const response = await fetch('/api/run_playbook', {
      method: 'POST',
      body: JSON.stringify({ playbookName })
    });
    // ... håndter respons og oppdater UI
  }
</script>

<button on:click={() => runPlaybook('my_playbook.yml')}>Kjør Playbook</button>