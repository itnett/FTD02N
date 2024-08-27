<script>
      import { onMount } from 'svelte';
      import { Terminal } from 'xterm';
      import 'xterm/css/xterm.css';

      onMount(() => {
        const terminal = new Terminal();
        terminal.open(document.getElementById('terminal'));
        // Simuler kommandoer og output
        terminal.write('$ ls -l\r\n');
        terminal.write('total 20\r\n');
        terminal.write('-rw-r--r-- 1 root root 1234 May 10 14:32 file.txt\r\n');
        // ...
      });
    </script>

    <div id="terminal"></div>