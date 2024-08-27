<script>
  import { onMount } from 'svelte';
  let cloudResources = [];

  onMount(async () => {
    const response = await fetch('/api/cloud-resources');
    cloudResources = await response.json();
  });
</script>

<main>
  <h1>Cloud Resource Dashboard</h1>
  <ul>
    {#each cloudResources as resource}
      <li>{resource.name}: {resource.status}</li>
    {/each}
  </ul>
</main>