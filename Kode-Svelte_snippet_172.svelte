<script>
  let questions = [
    { question: 'Hva er HTTP-statuskode 200?', options: ['OK', 'Feil', 'Flyttet'], answer: 'OK' }
  ];
  let currentQuestion = 0;
  let userAnswer = '';

  function checkAnswer() {
    if (userAnswer === questions[currentQuestion].answer) {
      alert('Riktig!');
    } else {
      alert('Feil.');
    }
  }
</script>

<main>
  <h1>IT-sertifisering Quiz</h1>
  <p>{questions[currentQuestion].question}</p>
  {#each questions[currentQuestion].options as option}
    <label>
      <input type="radio" bind:group={userAnswer} value={option} />
      {option}
    </label>
  {/each}
  <button on:click={checkAnswer}>Sjekk svar</button>
</main>