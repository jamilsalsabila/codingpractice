/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    let i = 1;
    let c = 0;
    while (i < nums.length) {
        let j = 1;
        while (i < nums.length && nums[i] === nums[i - 1]) {
            i++; j++;
        }
        if (j > 2) {
            for (let k = 0; k < j - 2; k++) {
                nums[i - 1 - k] = 999999;
                c++;
            }
        }
        i++;
    }
    nums.sort((a, b) => a - b);
    return nums.length - c;
};

console.log(removeDuplicates([1, 1, 1, 2, 2, 3]));
console.log(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]));