const calculateNumber = require("./1-calcul");
const assert = require('assert');

describe("calculateNumber", () => {
	assert.equal(calculateNumber('SUM', 1, 3), 4);
	assert.equal(calculateNumber('SUM', 1.9, 3), 5);
	assert.equal(calculateNumber('SUM', 1, 6.4), 7);
	assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
	assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);

    assert.equal(calculateNumber('SUBTRACT', 3.2, 1.8), 1);
	assert.equal(calculateNumber('SUBTRACT', 3, 1), 2);
	assert.equal(calculateNumber('SUBTRACT', 9.9, 0.9), 9);
	assert.equal(calculateNumber('SUBTRACT', 5.8, 0), 6);
	assert.equal(calculateNumber('SUBTRACT', 1.2, 3.7), -3);

	assert.equal(calculateNumber('DIVIDE', 9, 3.2), 3);
	assert.equal(calculateNumber('DIVIDE', 12, 3.8), 3);
	assert.equal(calculateNumber('DIVIDE', 11.9, 5.7), 2);
	assert.equal(calculateNumber('DIVIDE', 16.1, 3.6), 4);
	assert.equal(calculateNumber('DIVIDE', 9, 0.2), 'Error');
});
