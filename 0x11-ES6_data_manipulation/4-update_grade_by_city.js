function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const result = { ...student };
      const found = newGrades.find((grades) => grades.studentId === student.id);

      result.grade = found ? found.grade : 'N/A';

      return result;
    });
}

export default updateStudentGradeByCity;
