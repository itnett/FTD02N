<script>
     import { onMount } from 'svelte';
     import axios from 'axios';

     let networkData = [];

     async function fetchNetworkData() {
       const response = await axios.get('http://localhost:4000/api/network');
       networkData = response.data;
     }

     onMount(() => {
       fetchNetworkData();
     });
   </script>

   <main>
     <h1>Network Data</h1>
     <ul>
       {#each networkData as data}
         <li>{data.interface}: {data.traffic} bytes</li>
       {/each}
     </ul>
   </main>