const fs = require('fs');

function countStudents(db) {
  let data;
  const fields = {};

  try {
    data = fs.readFileSync(db);
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  data = data.toString().split('\n');
  data.shift();

  data.forEach((item) => {
    if (item) {
      const row = item.split(',');
      if (row[3] in fields) {
        fields[row[3]].push(row[0]);
      } else {
        fields[row[3]] = [row[0]];
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
}

module.exports = countStudents;
