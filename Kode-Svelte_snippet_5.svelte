<script>
  let names = ["Alice", "Bob", "Charlie"];
</script>

<ul>
  {#each names as name}
    <li>{name}</li>
  {/each}
</ul>