/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
    let carry = 1;
    let i = digits.length - 1;
    while (i > -1 && digits[i] + carry === 10) {
        digits[i] = 0;
        i--;
    }
    digits[i] += carry;
    if (i === -1) {
        digits.unshift(carry);
    }
    return digits;
};

console.log(plusOne([1, 2, 3]));
console.log(plusOne([4, 3, 2, 1]));
console.log(plusOne([9, 9]));
