<script>
  import Counter from './Counter.svelte';
  import { writable } from 'svelte/store';

  const count = writable(0);
</script>

<Counter {count} />
<Counter {count} />

<script>
  export let count;
</script>

<button on:click={() => count.update(n => n - 1)}>-</button>
<span>{ $count }</span>
<button on:click={() => count.update(n => n + 1)}>+</button>