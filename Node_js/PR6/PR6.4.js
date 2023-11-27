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
    // Find the data you want to rename
    const dataToRename = existingData.find(item => item.Name === 'John');

    if (dataToRename) {
      // Update the data with the new name
      dataToRename.Name = 'Jonathan';

      // Create a CSV writer
      const csvWriter = createObjectCsvWriter({
        path: csvFilePath,
        header: [
          { id: 'Name', title: 'Name' },
          { id: 'Age', title: 'Age' },
          { id: 'Location', title: 'Location' },
        ],
      });

      // Write the updated data back to the CSV file
      csvWriter.writeRecords(existingData)
        .then(() => {
          console.log('Data renamed in CSV.');
        })
        .catch((error) => {
          console.error('Error renaming data in CSV:', error);
        });
    } else {
      console.log('Data not found for renaming.');
    }
  });
