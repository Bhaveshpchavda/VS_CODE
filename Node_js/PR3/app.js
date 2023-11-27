// app.js
var  express = require('express');
var  path = require('path');
var  dateTimeModule = require('./DateTimeModule');

var  app = express();
var  PORT = process.env.PORT || 8080;

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/getDateTime', (req, res) => {
  var  currentDateTime = dateTimeModule.getCurrentDateTime();
  res.send(currentDateTime);
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
