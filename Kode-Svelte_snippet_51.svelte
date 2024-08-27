<script>
      let resources = [
        { name: 'Utvikler 1', availability: 40 },
        // ... flere ressurser
      ];

      let tasks = [
        { name: 'Oppgave A', effort: 20 },
        // ... flere oppgaver
      ];
    </script>

    <form on:submit|preventDefault={assignResources}>
      {#each tasks as task}
        <label for={task.name}>Tildel ressurser til {task.name}:</label>
        <select id={task.name} bind:value={task.assignedResource}>
          {#each resources as resource}
            <option value={resource.name}>{resource.name}</option>
          {/each}
        </select>
      {/each}
      <button type="submit">Lagre tildeling</button>
    </form>