// Eksempel på enkel input-validering i JavaScript
   function validateInput(input) {
       const regex = /^[a-zA-Z0-9]*$/;
       return regex.test(input);
   }