import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    readDatabase(process.argv[2])
      .then((table) => {
        const fields = ['This is the list of our students'];

        for (const key in table) {
          if (key) {
            fields.push(`Number of students in ${key}: ${table[key].length}. List: ${table[key].join(', ')}`);
          }
        }

        res.status(200).send(fields.join('\n'));
      })
      .catch(() => res.status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (!['CS', 'SWE'].includes(major)) {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(process.argv[2])
      .then((table) => res.status(200).send(`List: ${table[major].join(', ')}`))
      .catch(() => res.status(500).send('Cannot load the database'));
  }
}

export default StudentsController;
