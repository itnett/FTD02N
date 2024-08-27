<script>
     import axios from 'axios';
     import { onMount } from 'svelte';

     let items = [];
     let newItem = '';

     async function fetchItems() {
       const response = await axios.get('http://localhost:4000/api/items');
       items = response.data;
     }

     async function addItem() {
       const response = await axios.post('http://localhost:4000/api/items', { id: Date.now().toString(), name: newItem });
       items.push(response.data);
       newItem = '';
     }

     async function deleteItem(id) {
       await axios.delete(`http://localhost:4000/api/items/${id}`);
       items = items.filter(item => item.id !== id);
     }

     onMount(() => {
       fetchItems();
     });
   </script>

   <main>
     <h1>CRUD App</h1>
     <input type="text" bind:value={newItem} placeholder="Add new item" />
     <button on:click={addItem}>Add Item</button>
     <ul>
       {#each items as item (item.id)}
         <li>
           {item.name}
           <button on:click={() => deleteItem(item.id)}>Delete</button>
         </li>
       {/each}
     </ul>
   </main>