const fs = require('fs').promises;

function countStudents(path) {
  return fs
    .readFile(path, 'utf8')
    .then((content) => content.split('\n'))
    .then((students) => {
      let numberOfStudents = 0;
      const studentsOnFields = {};
      const logs = [];
      let finalText = '';

      for (let i = 1; i < students.length; i += 1) {
        const student = students[i];
        if (student) {
          const [firstName, , , field] = students[i].split(',');

          if (studentsOnFields[field]) {
            studentsOnFields[field].push(firstName);
          } else {
            studentsOnFields[field] = [firstName];
          }

          numberOfStudents += 1;
        }
      }

      logs.push(`Number of students: ${numberOfStudents}`);
      for (const [key, value] of Object.entries(studentsOnFields)) {
        logs.push(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
      }

      for (const log of logs) {
        console.log(log);
      }

      finalText = logs.join('\n');

      return (finalText);
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
