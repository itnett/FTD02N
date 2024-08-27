<script>
      import { onMount } from 'svelte';
      import { subscribe } from 'svelte/store';
      import { alertStore } from './alertStore';

      let alerts = [];

      onMount(() => {
        const unsubscribe = alertStore.subscribe(value => {
          alerts = value;
        });
        return () => unsubscribe();
      });
    </script>

    <h2>Varsler</h2>
    <ul>
      {#each alerts as alert}
        <li>{alert.timestamp} - {alert.message}</li>
      {/each}
    </ul>