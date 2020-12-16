export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const r = mathFunction();
    queue.push(r);
  } catch (e) {
    queue.push(e.toString());
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
