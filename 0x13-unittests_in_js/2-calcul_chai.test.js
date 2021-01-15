const { ShouldThrow, expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
  it('1 + 3', () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4)
  })
  it('1 + 3.7', () => {
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5)
  })
  it('1.2 + 3.7', () => {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5)
  })
  it('1.5 + 3.7', () => {
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6)
  })
  it('1.1 + 1.2', () => {
    expect(calculateNumber('SUM', 1.1, 1.2)).to.equal(2)
  })
  it('1.4 - 4.5', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4)
  })
  it('1.4 / 4.5', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2)
  })
  it('1.4 / 0', () => {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error')
  })
})
