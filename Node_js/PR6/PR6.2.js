// Practical 6.2
// Add Data in csv
const fs = require('fs');
const { createObjectCsvWriter } = require('csv-writer');

const csvFilePath = 'data.csv';

const csvWriter = createObjectCsvWriter({
  path: csvFilePath,
  header: [
    { id: 'Name', title: 'Name' },
    { id: 'Age', title: 'Age' },
    { id: 'Location', title: 'Location' },
  ],
  append: true,
});

const newData = [
  { Name: 'Eva', Age: 29, Location: 'Miami' },
  { Name: 'David', Age: 33, Location: 'Seattle' },
];

csvWriter.writeRecords(newData)
  .then(() => {
    console.log('Data added to CSV.');
  })
  .catch((error) => {
    console.error('Error adding data to CSV:', error);
  });
