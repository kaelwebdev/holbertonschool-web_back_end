const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
  it('1 + 3', () => {
    assert.equal(calculateNumber('SUM', 1, 3), 4)
  })
  it('1 + 3.7', () => {
    assert.equal(calculateNumber('SUM', 1, 3.7), 5)
  })
  it('1.2 + 3.7', () => {
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5)
  })
  it('1.5 + 3.7', () => {
    assert.equal(calculateNumber('SUM', 1.5, 3.7), 6)
  })
  it('1.1 + 1.2', () => {
    assert.equal(calculateNumber('SUM', 1.1, 1.2), 2)
  })
  it('1 - 3', () => {
    assert.equal(calculateNumber('SUBTRACT', 1, 3), 4)
  })
  it('1 - 3.7', () => {
    assert.equal(calculateNumber('SUBTRACT', 1, 3.7), 5)
  })
  it('1.2 - 3.7', () => {
    assert.equal(calculateNumber('SUBTRACT', 1.2, 3.7), 5)
  })
  it('1.5 - 3.7', () => {
    assert.equal(calculateNumber('SUBTRACT', 1.5, 3.7), 6)
  })
  it('1.1 - 1.2', () => {
    assert.equal(calculateNumber('SUBTRACT', 1.1, 1.2), 2)
  })

})
