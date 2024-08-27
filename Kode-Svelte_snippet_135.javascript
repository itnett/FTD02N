const express = require('express');
   const bodyParser = require('body-parser');
   const cors = require('cors');
   const sqlite3 = require('sqlite3').verbose();

   const app = express();
   app.use(bodyParser.json());
   app.use(cors());

   const db = new sqlite3.Database('./database.db');

   app.get('/api/items', (req, res) => {
     db.all('SELECT * FROM items', [], (err, rows) => {
       if (err) {
         throw err;
       }
       res.json(rows);
     });
   });

   app.post('/api/items', (req, res) => {
     const { id, name } = req.body;
     db.run('INSERT INTO items (id, name) VALUES (?, ?)', [id, name], function(err) {
       if (err) {
         throw err;
       }
       res.status(201).json({ id, name });
     });
   });

   app.delete('/api/items/:id', (req, res) => {
     const id = req.params.id;
     db.run('DELETE FROM items WHERE id = ?', id, function(err) {
       if (err) {
         throw err;
       }
       res.status(204).end();
     });
   });

   const PORT = 4000;
   app.listen(PORT, () => {
     console.log(`Server is running on http://localhost:${PORT}`);
   });