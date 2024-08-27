const fs = require('fs');

// Lese fra en fil
fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Skrive til en fil
fs.writeFile('example.txt', 'Dette er en test.', (err) => {
  if (err) throw err;
  console.log('Filen er oppdatert.');
});