<script>
      import { onMount } from 'svelte';

      let resourceUsage = [];

      onMount(async () => {
        const response = await fetch('/api/resource_usage');
        resourceUsage = await response.json();
      });
    </script>

    <h2>Ressursbruk</h2>
    <table>
      <tr>
        <th>Ressurs</th>
        <th>Bruk</th>
      </tr>
      {#each resourceUsage as resource}
        <tr>
          <td>{resource.name}</td>
          <td>{resource.usage}%</td>
        </tr>
      {/each}
    </table>