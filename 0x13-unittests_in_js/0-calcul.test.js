const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('correctly adds 1 and 3', () => {
    assert.equal(calculateNumber(1, 3), 4)
  })
  it('correctly adds 1 and 3.7', () => {
    assert.equal(calculateNumber(1, 3.7), 5)
  })
  it('correctly adds 1.2 and 3.7', () => {
    assert.equal(calculateNumber(1.2, 3.7), 5)
  })
  it('correctly adds 1.5 and 3.7', () => {
    assert.equal(calculateNumber(1.5, 3.7), 6)
  })
  it('negative number', () => {
    assert.equal(calculateNumber(-1.5, 1.5), 1)
  })
  it('negative number + negative number', () => {
    assert.equal(calculateNumber(-1, -1), -2)
  })
})
