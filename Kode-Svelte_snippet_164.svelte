<script>
  let currentSlide = 0;
  const slides = [
    "Velkommen til vår presentasjon",
    "Svelte er et kraftig verktøy for utvikling",
    "Takk for oppmerksomheten"
  ];

  function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
  }
</script>

<main>
  <h1>{slides[currentSlide]}</h1>
  <button on:click={nextSlide}>Neste slide</button>
</main>