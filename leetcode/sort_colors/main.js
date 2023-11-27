/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
    for (let i = 1; i < nums.length; i++) {
        let j = i;
        while (j > 0) {
            if (j % 2 === 1) {
                if (nums[j] > nums[Math.floor(j / 2)]) {
                    [nums[j], nums[Math.floor(j / 2)]] = [nums[Math.floor(j / 2)], nums[j]];
                }
                j = Math.floor(j / 2);
            }
            if (j % 2 === 0) {
                if (nums[j] > nums[Math.floor(j / 2) - 1]) {
                    [nums[j], nums[Math.floor(j / 2) - 1]] = [nums[Math.floor(j / 2) - 1], nums[j]];
                }
                j = Math.floor(j / 2) - 1;
            }
        }
    }
    for (let i = nums.length - 1; i > 0; i--) {
        let j = 0;
        [nums[i], nums[j]] = [nums[j], nums[i]];
        while (j < Math.floor((i - 1) / 2)) {
            let k = (nums[j * 2 + 1] < nums[j * 2 + 2]) ? j * 2 + 2 : j * 2 + 1;
            if (nums[j] < nums[k]) {
                [nums[j], nums[k]] = [nums[k], nums[j]];
                j = k;
            } else {
                break;
            }
        }
        while (j < Math.floor(i / 2)) {
            let k = j * 2 + 1;
            if (nums[j] < nums[k]) {
                [nums[j], nums[k]] = [nums[k], nums[j]];
                j = k;
            } else {
                break;
            }
        }
    }
    return nums;
};

console.log(sortColors([1, 2, 3, 4, 5, 6]));
console.log(sortColors([2, 0, 2, 1, 1, 0]));
console.log(sortColors([1, 2, 0]));
console.log(sortColors([]));
console.log(sortColors([2, 1]));
console.log(sortColors([2]));
console.log(sortColors([1, 2, 0, 4, -100]));


/* Solusi Lain
var sortColors = function(nums) {
    // Keep three indices beg = 0, mid = 0 and end = nums.length-1...
    // There are four ranges, 1 to beg (the range containing 0), beg to mid (the range containing 1), mid to end (the range containing unknown elements) and end to nums.length (the range containing 2)...
    let beg = 0; 
    let end = nums.length - 1; 
    let mid = 0;
    let temp = 0;
    // Traverse the array from start to end and mid is less than end...
    while (mid <= end) {
        // If the element is 0...
        if(nums[mid] == 0) {
            // swap the element with the element at index beg...
            temp = nums[beg]; 
            nums[beg] = nums[mid]; 
            nums[mid] = temp;
            // Update beg = beg + 1 and mid = mid + 1...
            beg++; 
            mid++; 
        }
        // If the element is 1 then update mid = mid + 1...
        else if(nums[mid] == 1) {
            mid++; 
        }
        // If the element is 2...
        else {
            // Swap the element with the element at index end...
            temp = nums[mid]; 
            nums[mid] = nums[end]; 
            nums[end] = temp;
            // Update end = end – 1...
            end--;
        }      
    }
};
*/