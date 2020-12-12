export default function appendToEachArrayValue(array, appendString) {
  const aCp = array;

  for (const value of array) {
    const idx = array.indexOf(value);
    aCp[idx] = appendString + value;
  }

  return aCp;
}
