class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');

    if (typeof length !== 'number') throw TypeError('Length must be a number');

    if (!Array.isArray(students)) throw TypeError('students must be an Array');

    if (students.find((student) => typeof student !== 'string')) {
      throw TypeError('student must be a String');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(name) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    this._name = name;
  }

  get name() {
    return this._name;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    }

    this._length = length;
  }

  get length() {
    return this._length;
  }

  set students(students) {
    if (!Array.isArray(students)) {
      throw TypeError('students must be an Array');
    }

    if (students.find((student) => typeof student !== 'string')) {
      throw TypeError('student must be a String');
    }

    this._students = students;
  }

  get students() {
    return this._students;
  }
}

export default HolbertonCourse;
