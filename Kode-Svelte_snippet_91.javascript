const express = require('express');
   const bodyParser = require('body-parser');
   const cors = require('cors');

   const app = express();
   app.use(bodyParser.json());
   app.use(cors());

   let items = [];

   app.get('/items', (req, res) => {
     res.json(items);
   });

   app.post('/items', (req, res) => {
     const newItem = req.body;
     items.push(newItem);
     res.status(201).json(newItem);
   });

   app.delete('/items/:id', (req, res) => {
     const id = req.params.id;
     items = items.filter(item => item.id !== id);
     res.status(204).end();
   });

   const PORT = 4000;
   app.listen(PORT, () => {
     console.log(`Server is running on http://localhost:${PORT}`);
   });