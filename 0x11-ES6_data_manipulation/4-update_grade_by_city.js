export default function updateStudentGradeByCity(students, city, newgrades) {
  const StudentsByCity = students.filter((student) => student.location === city);
  return StudentsByCity.map((student) => {
    const foundedId = newgrades.filter((obj) => student.id === obj.studentId);
    if (foundedId[0]) {
      return { ...student, grade: foundedId[0].grade };
    }
    return { ...student, grade: 'N/A' };
  });
}
