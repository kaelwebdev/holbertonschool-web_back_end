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
  it('negative number + positive number', () => {
    assert.equal(calculateNumber(-1.5, 1.5), 1)
  })
  it('negative number + negative number', () => {
    assert.equal(calculateNumber(-1, -1), -2)
  })
  it('zero + zero', () => {
    assert.equal(calculateNumber(0, 0), 0)
  })
  it('2.999 + 1', () => {
    assert.equal(calculateNumber(2.99, 1), 4)
  })
  it('1.1 + 0', () => {
    assert.equal(calculateNumber(1.1, 0), 1)
  })
  it('-0.19 + 0', () => {
    assert.equal(calculateNumber(-0.19, 0), 0)
  })
})
