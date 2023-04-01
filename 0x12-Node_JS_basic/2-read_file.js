const fs = require('fs');

function countStudents(path) {
  let content = null;
  try {
    content = fs.readFileSync(path, 'utf-8');
  } catch (e) {
    throw new Error('Cannot load the database');
  }

  const students = content.split('\n');

  let numberOfStudents = 0;
  const studentsOnFields = {};

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

  console.log(`Number of students: ${numberOfStudents}`);
  for (const [key, value] of Object.entries(studentsOnFields)) {
    console.log(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
  }
}

module.exports = countStudents;
