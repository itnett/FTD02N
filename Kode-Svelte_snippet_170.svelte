<script>
  let code = 'console.log("Hello, world!");';

  function runCode() {
    eval(code);
  }
</script>

<main>
  <h1>Kode-editor</h1>
  <textarea bind:value={code}></textarea>
  <button on:click={runCode}>Kjør kode</button>
</main>