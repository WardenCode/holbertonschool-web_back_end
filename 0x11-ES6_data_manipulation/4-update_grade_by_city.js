function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const result = {
        ...student,
        grade: 'N/A',
      };
      const found = newGrades.find((grades) => grades.studentId === student.id);

      if (found) result.grade = found.grade;

      return result;
    });
}

export default updateStudentGradeByCity;
