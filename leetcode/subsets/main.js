/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
    let r = [];
    r.push([]);
    for (let i = 0; i < nums.length; i++) {
        let rL = r.length;
        for (let j = 0; j < rL; j++) {
            const tmp = Array.from(r[j]);
            tmp.push(nums[i]);
            r.push(tmp);
        }
    }
    return r;
};

console.log(subsets([1, 2]));
console.log(subsets([0]));
console.log(subsets([1, 2, 3]));
console.log(subsets([3, 2, 4, 1]));