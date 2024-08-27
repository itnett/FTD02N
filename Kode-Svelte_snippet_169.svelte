<script>
  import { onMount } from 'svelte';
  let items = [];
  let newItem = '';

  onMount(async () => {
    const response = await fetch('/api/items');
    items = await response.json();
  });

  async function addItem() {
    const response = await fetch('/api/items', {
      method: 'POST',
      body: JSON.stringify({ name: newItem }),
      headers: {
        'Content-Type': 'application/json'
      }
    });
    items.push(await response.json());
    newItem = '';
  }

  async function deleteItem(id) {
    await fetch(`/api/items/${id}`, { method: 'DELETE' });
    items = items.filter(item => item.id !== id);
  }
</script>

<main>
  <h1>CRUD Applikasjon</h1>
  <input type="text" bind:value={newItem} placeholder="Nytt element" />
  <button on:click={addItem}>Legg til</button>
  <ul>
    {#each items as item (item.id)}
      <li>
        {item.name}
        <button on:click={() => deleteItem(item.id)}>Slett</button>
      </li>
    {/each}
  </ul>
</main>