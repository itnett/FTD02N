<script>
      let vmCount = 2;
      let storageSize = 50;

      function scaleUp() {
        vmCount++;
      }

      function increaseStorage() {
        storageSize += 10;
      }
    </script>

    <button on:click={scaleUp}>Øk antall VM-er</button>
    <button on:click={increaseStorage}>Øk lagringsplass</button>

    <p>Antall VM-er: {vmCount}</p>
    <p>Lagringsplass: {storageSize} GB</p>