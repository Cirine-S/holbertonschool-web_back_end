export default function iterateThroughObject(reportWithIterator) {
  const arr = [];
  for (const it of reportWithIterator) arr.push(it);
  return arr.join(' | ');
}
