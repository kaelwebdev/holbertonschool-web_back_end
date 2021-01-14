const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
    it('correctly adds 1 and 3', () => {
        assert.equal(calculateNumber(1, 3), 4)
    })
})
