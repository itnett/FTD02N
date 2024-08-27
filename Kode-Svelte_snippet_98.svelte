<script>
     // Legg til variabel og funksjon for redigering
     let editedItem = null;

     function editItem(item) {
       editedItem = { ...item };
     }

     async function saveItem() {
       await axios.put(`http://localhost:4000/items/${editedItem.id}`, editedItem);
       items = items.map(item => (item.id === editedItem.id ? editedItem : item));
       editedItem = null;
     }
   </script>

   <main>
     <!-- Eksisterende kode -->
     <ul>
       {#each items as item (item.id)}
         <li>
           {#if editedItem && editedItem.id === item.id}
             <input type="text" bind:value={editedItem.name} />
             <button on:click={saveItem}>Save</button>
           {:else}
             {item.name}
             <button on:click={() => editItem(item)}>Edit</button>
             <button on:click={() => deleteItem(item.id)}>Delete</button>
           {/if}
         </li>
       {/each}
     </ul>
   </main>