// Practical 6.1
// Read Data From csv
const fs = require('fs');
const csv = require('csv-parser');

const csvFilePath = 'data.csv';

const results = [];

fs.createReadStream(csvFilePath)
  .pipe(csv())
  .on('data', (data) => {
    results.push(data);
  })
  .on('end', () => {
    console.log('Data read from CSV:');
    console.log(results);
  });
