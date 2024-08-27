<script>
  import { onMount } from 'svelte';

  let name = '';
  let greeting = '';
  let apiData = [];

  async function fetchGreeting() {
    try {
      const response = await fetch('/api/greet?name=' + encodeURIComponent(name));
      const data = await response.json();
      greeting = data.greeting;
    } catch (error) {
      console.error('API-feil:', error);
      greeting = 'Noe gikk galt. Prøv igjen senere.';
    }
  }

  onMount(async () => {
    try {
      const response = await fetch('/api/data');
      apiData = await response.json();
    } catch (error) {
      console.error('API-feil:', error);
    }
  });
</script>

<input type="text" bind:value={name} placeholder="Skriv inn navnet ditt">
<button on:click={fetchGreeting}>Hent hilsen</button>

{#if greeting}
  <p>{greeting}</p>
{/if}

<h2>Data fra API:</h2>
<ul>
  {#each apiData as item}
    <li>{item.id}: {item.value}</li>
  {/each}
</ul>