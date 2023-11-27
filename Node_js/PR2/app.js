const express = require('express');
const path = require('path');

const app = express();
const port = 8080;

app.get('/practical2.1', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/practical2.2', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index1.html'));
});

app.use(express.static(path.join(__dirname, 'public')));

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
