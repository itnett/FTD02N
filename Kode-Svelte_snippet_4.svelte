<script>
  let status = "Av";

  function toggleStatus() {
    status = status === "Av" ? "På" : "Av";
  }
</script>

<button on:click={toggleStatus}>Toggle</button>
<p>{status}</p>