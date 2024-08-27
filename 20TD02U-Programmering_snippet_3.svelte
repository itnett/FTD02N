<script>
  let password = '';
  let passwordStrength = 'Svak';

  $: if (password.length >= 12 && /\d/.test(password) && /[A-Z]/.test(password)) {
    passwordStrength = 'Sterk';
  } else if (password.length >= 8) {
    passwordStrength = 'Middels';
  }
</script>

<input type="password" bind:value={password}>
<p>Passordstyrke: {passwordStrength}</p>