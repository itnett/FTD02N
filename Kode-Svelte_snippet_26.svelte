<script>
      import { onMount } from 'svelte';

      let securityEvents = [];

      onMount(async () => {
        const response = await fetch('/api/security_events');
        securityEvents = await response.json();
      });
    </script>

    <h2>Sikkerhetshendelser</h2>
    <ul>
      {#each securityEvents as event}
        <li>{event.timestamp} - {event.type}</li>
      {/each}
    </ul>