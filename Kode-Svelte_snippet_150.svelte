<script>
     import { onMount } from 'svelte';
     import axios from 'axios';

     let logs = [];

     async function fetchLogs() {
       const response = await axios.get('http://localhost:4000/api/logs');
       logs = response.data;
     }

     onMount(() => {
       fetchLogs();
     });
   </script>

   <main>
     <h1>Security Logs</h1>
     <ul>
       {#each logs as log}
         <

li>{log.timestamp}: {log.message}</li>
       {/each}
     </ul>
   </main>