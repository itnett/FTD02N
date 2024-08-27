<script>
  let incidents = [
    { id: 1, title: 'Server nede', status: 'Åpen' },
    { id: 2, title: 'Treg nettverkstilkobling', status: 'Under behandling' },
    // ...
  ];
</script>

<h2>Åpne hendelser</h2>
<ul>
  {#each incidents as incident (incident.id)}
    <li>
      {incident.title} - {incident.status}
    </li>
  {/each}
</ul>