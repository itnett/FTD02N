<script>
  import Greeting from './Greeting.svelte';
</script>

<Greeting name="Emma" />

<script>
  export let name;
</script>

<h2>Hei, {name}!</h2>