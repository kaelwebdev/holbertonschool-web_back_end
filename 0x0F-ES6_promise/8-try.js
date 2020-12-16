export default function divideFunction(numerator, denominator) {
  const r = numerator / denominator;
  if (r !== Infinity) {
    return r;
  }
  throw Error('cannot divide by 0');
}
