const fs = require('fs');

function countStudents(db) {
  return new Promise((resolve, reject) => {
    const fields = {};
    fs.readFile(db, 'utf8', (err, csvFile) => {
      if (err) {
        reject(Error('Cannot load the database'));
      }
      const data = csvFile.toString().split('\n');
      data.shift();

      data.forEach((item) => {
        if (item) {
          const idx = item.split(',');
          if (idx[3] in fields) {
            fields[idx[3]].push(idx[0]);
          } else {
            fields[idx[3]] = [idx[0]];
          }
        }
      });

      console.log(`Number of students: ${data.length}`);

      for (const field in fields) {
        if (field) {
          const list = fields[field];
          console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
        }
      }
      resolve();
    });
  });
}

module.exports = countStudents;
