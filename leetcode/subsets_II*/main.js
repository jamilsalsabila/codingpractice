/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function (nums) {
    nums.sort((a, b) => a - b);
    let r = [[]];
    for (let i = 0; i < nums.length; i++) {

        while (nums[i] === nums[i - 1] && i + 1 < nums.length && nums[i] === nums[i + 1]) {
            i = i + 1;
            continue;
        }
        let tmp1 = [[nums[i]]];
        for (let j = i + 1; j < nums.length; j++) {
            let tmp2 = Array.from(tmp1[j - 1 - i]);
            tmp2.push(nums[j]);
            tmp1.push(tmp2);
        }
        if (nums[i] === nums[i - 1]) tmp1 = tmp1.slice(1);
        r.push(...tmp1);
    }
    return r;
};

console.log(subsetsWithDup([1, 1, 2, 2, 2, 3, 5, 5, 4]));
console.log(subsetsWithDup([0]));