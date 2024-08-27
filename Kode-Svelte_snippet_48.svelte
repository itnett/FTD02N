<script>
      import { onMount } from 'svelte';
      import Gantt from 'frappe-gantt'; // Eller et annet Gantt-bibliotek

      let tasks = [
        { id: 'task1', name: 'Kravspesifikasjon', start: '2024-01-01', end: '2024-01-15', progress: 100 },
        { id: 'task2', name: 'Utvikling', start: '2024-01-16', end: '2024-02-29', progress: 60, dependencies: ['task1'] },
        // ... flere oppgaver
      ];

      onMount(() => {
        new Gantt('#gantt', tasks);
      });
    </script>

    <div id="gantt"></div>