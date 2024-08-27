<script>
      async function hentData() {
        const respons = await fetch('https://api.eksempel.no/data');
        const data = await respons.json();
        // ... bruk dataene
      }
    </script>