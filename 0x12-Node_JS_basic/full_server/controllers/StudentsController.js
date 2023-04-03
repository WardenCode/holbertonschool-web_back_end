import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response, path) {
    readDatabase(path)
      .then((table) => {
        const fields = ['This is the list of our students'];

        for (const key in table) {
          if (key) {
            fields.push(`Number of students in ${key}: ${table[key].length}. List: ${table[key].join(', ')}`);
          }
        }

        response.status(200).send(fields.join('\n'));
      })
      .catch(() => response.status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(request, response, path) {
    const { major } = request.params;

    if (!['CS', 'SWE'].includes(major)) {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(path)
      .then((table) => response.status(200).send(`List: ${table[major].join(', ')}`))
      .catch(() => response.status(500).send('Cannot load the database'));
  }
}

export default StudentsController;
