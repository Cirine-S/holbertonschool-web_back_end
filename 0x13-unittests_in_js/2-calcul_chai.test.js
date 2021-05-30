const calculateNumber = require("./2-calcul_chai");
const chai = require('chai');
let expect = chai.expect;


describe("calculateNumber", () => {
	expect(calculateNumber('SUM', 1.9, 1)).to.equal(3);
	expect(calculateNumber('SUM', 1, 6.4)).to.equal(7);
	expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);

	expect(calculateNumber('SUBTRACT', 3.2, 1.8)).to.equal(1);
	expect(calculateNumber('SUBTRACT', 9.9, 0.9)).to.equal(9);
	expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);

	expect(calculateNumber('DIVIDE', 9, 3.2)).to.equal(3);
	expect(calculateNumber('DIVIDE', 16.1, 3.6)).to.equal(4);
	expect(calculateNumber('DIVIDE', 9, 0.2)).to.equal('Error');
});
