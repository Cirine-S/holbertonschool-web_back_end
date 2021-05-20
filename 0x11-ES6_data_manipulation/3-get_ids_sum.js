export default function getStudentIdsSum(students) {
  const reducer = (accumulator, currentValue) => accumulator + currentValue;
  const IdsArray = students.map((student) => student.id);
  return IdsArray.reduce(reducer);
}
