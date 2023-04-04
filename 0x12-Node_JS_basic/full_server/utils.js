const fs = require('fs').promises;

function readDatabase(path) {
  return fs
    .readFile(path, 'utf-8')
    .then((content) => content.split('\n'))
    .then((data) => {
      const students = data.map((student) => student.split(','));
      const fields = {};

      for (let i = 1; i < students.length; i += 1) {
        if (students[i].length === 4) {
          const [firstName, , , field] = students[i];
          if (!fields[field]) fields[field] = [firstName];
          else fields[field].push(firstName);
        }
      }

      return fields;
    })
    .catch((err) => {
      throw new Error(err);
    });
}

export default readDatabase;
