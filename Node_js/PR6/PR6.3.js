const fs = require('fs');
const { createObjectCsvWriter } = require('csv-writer');

const csvFilePath = 'data.csv';

// Load existing data from the CSV file
const existingData = [];
fs.createReadStream(csvFilePath)
  .on('data', (data) => {
    existingData.push(data);
  })
  .on('end', () => {
    // Filter out the data you want to delete
    const dataToDelete = existingData.filter(item => item.Name !== 'David');

    // Create a CSV writer
    const csvWriter = createObjectCsvWriter({
      path: csvFilePath,
      header: [
        { id: 'Name', title: 'Name' },
        { id: 'Age', title: 'Age' },
        { id: 'Location', title: 'Location' },
      ],
    });

    // Write the filtered data back to the CSV file
    csvWriter.writeRecords(dataToDelete)
      .then(() => {
        console.log('Data deleted from CSV.');
      })
      .catch((error) => {
        console.error('Error deleting data from CSV:', error);
      });
  });
