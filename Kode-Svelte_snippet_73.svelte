<script>
      import { onMount } from 'svelte';
      import { Terminal } from 'xterm';

      onMount(() => {
        const terminal = new Terminal();
        terminal.open(document.getElementById('terminal'));
        terminal.write('Router> enable\r\n'); // Simulert output
      });
    </script>

    <div id="terminal"></div>