<script>
  let a = 1;
  let b = 1;
  let c = 1;

  function calculateRoots() {
    const discriminant = b * b - 4 * a * c;
    const root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
    const root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
    return { root1, root2 };
  }
</script>

<main>
  <h1>Kvadratisk ligningsløser</h1>
  <input type="number" bind:value={a} placeholder="a" />
  <input type="number" bind:value={b} placeholder="b" />
  <input type="number" bind:value={c} placeholder="c" />
  <p>Løsningene er {calculateRoots().root1} og {calculateRoots().root2}</p>
</main>