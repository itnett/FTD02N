<script>
      import { onMount } from 'svelte';

      let projectProgress = 0;
      let tasksCompleted = 0;
      let totalTasks = 0;

      onMount(async () => {
        const response = await fetch('/api/project_status');
        const data = await response.json();
        projectProgress = data.progress;
        tasksCompleted = data.tasksCompleted;
        totalTasks = data.totalTasks;
      });
    </script>

    <h2>Prosjektstatus</h2>
    <p>Fremdrift: {projectProgress}%</p>
    <p>Oppgaver fullført: {tasksCompleted} / {totalTasks}</p>