export default function appendToEachArrayValue (array, appendString) {
  let idx = 0;

  for (const element of array) {
    array[idx] = `${appendString}${element}`;
    idx++;
  }

  return array;
}
