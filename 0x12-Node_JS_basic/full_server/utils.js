import { readFile } from 'fs/promises';

function readDatabase(path) {
  return readFile(path, 'utf-8')
    .then((content) => content.split('\n'))
    .then((data) => {
      const students = data.map((student) => student.split(','));
      const result = {};

      for (let i = 1; i < students.length; i += 1) {
        if (students[i].length === 4) {
          const [firstName, , , field] = students[i];
          if (!result[field]) result[field] = [firstName];
          else result[field].push(firstName);
        }
      }

      return result;
    })
    .catch(() => Error('Cannot load the database'));
}

export default readDatabase;
