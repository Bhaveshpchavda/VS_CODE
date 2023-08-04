const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Serve index.html for Practical 2.1
app.get('/practical2.1', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Serve index1.html for Practical 2.2
app.get('/practical2.2', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index1.html'));
});

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
