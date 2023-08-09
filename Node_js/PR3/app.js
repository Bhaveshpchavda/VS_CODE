// app.js
const express = require('express');
const path = require('path');
const dateTimeModule = require('./DateTimeModule');

const app = express();
const PORT = process.env.PORT || 8080;

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/getDateTime', (req, res) => {
  const currentDateTime = dateTimeModule.getCurrentDateTime();
  res.send(currentDateTime);
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
