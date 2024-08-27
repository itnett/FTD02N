<script>
  let name = '';
  let greeting = '';

  function greet() {
    greeting = `Hello, ${name}!`;
  }
</script>

<input type="text" bind:value={name} placeholder="Enter your name">
<button on:click={greet}>Greet</button>

{#if greeting}
  <p>{greeting}</p>
{/if}