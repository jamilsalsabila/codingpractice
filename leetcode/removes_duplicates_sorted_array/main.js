/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    let tmp = nums[0];
    let c = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== tmp) {
            tmp = nums[i];
            [nums[c], nums[i]] = [nums[i], nums[c]];
            c += 1;
        }
    }
    // console.log(nums);
    return c;
};

console.log(removeDuplicates([1, 1, 2]));
console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));