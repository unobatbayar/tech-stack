require('dotenv').config
const express = require('express');
const app = express();
const port = process.env.port || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.get('/api/items', (req, res) => {
  res.json([
    {id: 1, name:'Item One'},
    {id: 1, name:'Item Two'},
    {id: 1, name:'Item Three'}
  ]);
});

app.post('/api/items', (req, res) => {
  const newItem = req.body;
  newItem.id = Date.now();
  res.status(201).json(newItem);
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});