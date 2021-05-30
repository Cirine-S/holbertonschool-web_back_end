const calculateNumber = require("./0-calcul");
const assert = require('assert');

describe("calculateNumber", () => {
	assert.equal(calculateNumber(1, 3), 4)
	assert.equal(calculateNumber(1.9, 3), 5);
	assert.equal(calculateNumber(1.8, 3.2), 5);
	assert.equal(calculateNumber(1, 6.4), 7);
	assert.equal(calculateNumber(1, 3.7), 5);
	assert.equal(calculateNumber(1.2, 3.7), 5);
	assert.equal(calculateNumber(1.5, 3.7), 6);
});
