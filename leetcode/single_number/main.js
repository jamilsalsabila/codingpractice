/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    let xor = 0;
    nums.forEach((val) => {
        xor ^= val;
    });
    return xor;
};

console.log(singleNumber([2, 2, 1]));