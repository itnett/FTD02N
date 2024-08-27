<script>
      // ... hent data fra API
      let tasks = [/* ... */];
      let resources = [/* ... */];
    </script>

    <h2>Oppgaver</h2>
    <ul>
      {#each tasks as task}
        <li>{task.name} - {task.status}</li>
      {/each}
    </ul>

    <h2>Ressurser</h2>
    <ul>
      {#each resources as resource}
        <li>{resource.name} - {resource.availability}</li>
      {/each}
    </ul>