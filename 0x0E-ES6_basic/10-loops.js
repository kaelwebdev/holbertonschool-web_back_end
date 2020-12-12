export default function appendToEachArrayValue(array, appendString) {
  const aCp = array;

  for (const [idx, value] of array.entries()) {
    aCp[idx] = appendString + value;
  }

  return aCp;
}
