<script>
  import { onMount } from 'svelte';
  import Gantt from 'frappe-gantt';

  let tasks = [
    {
      id: 'Task 1',
      name: 'Task 1',
      start: '2023-06-01',
      end: '2023-06-05',
      progress: 20
    },
    {
      id: 'Task 2',
      name: 'Task 2',
      start: '2023-06-06',
      end: '2023-06-10',
      progress: 50
    }
  ];

  onMount(() => {
    new Gantt('#gantt', tasks);
  });
</script>

<main>
  <h1>Prosjektledelse</h1>
  <div id="gantt"></div>
</main>