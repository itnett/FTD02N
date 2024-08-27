<script>
     import { onMount } from 'svelte';
     import axios from 'axios';

     let azureResources = [];
     let awsResources = [];

     async function fetchAzureResources() {
       const response = await axios.get('/api/azure/resources');
       azureResources = response.data;
     }

     async function fetchAwsResources() {
       const response = await axios.get('/api/aws/resources');
       awsResources = response.data;
     }

     onMount(() => {
       fetchAzureResources();
       fetchAwsResources();
     });
   </script>

   <main>
     <h1>Hybrid Cloud Dashboard</h1>
     <h2>Azure Resources</h2>
     <ul>
       {#each azureResources as resource}
         <li>{resource.name} - {resource.type}</li>
       {/each}
     </ul>
     <h2>AWS Resources</h2>
     <ul>
       {#each awsResources as resource}
         <li>{resource.name} - {resource.type}</li>
       {/each}
     </ul>
   </main>