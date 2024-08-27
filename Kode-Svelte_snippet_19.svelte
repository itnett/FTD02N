<script>
  import { writable } from 'svelte/store';

  const count = writable(0);

  function increment() {
    count.update(n => n + 1);
  }
</script>

<button on:click={increment}>
  Clicked {$count} { $count === 1 ? 'time' : 'times'}
</button>