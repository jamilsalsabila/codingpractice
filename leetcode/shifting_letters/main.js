/**
 * @param {string} s
 * @param {number[]} shifts
 * @return {string}
 */
var shiftingLetters = function (s, shifts) {
    let total = shifts.reduce((a, b) => a + b);
    let result = [];

    for (let i = 0; i < s.length; i++) {
        let new_char = String.fromCharCode(((s.charCodeAt(i) - 97 + total) % 26) + 97);
        result.push(new_char);
        total = total - shifts[i];
    }

    return result.reduce((a, b) => a + b);
};

console.log(shiftingLetters("aaa", [1, 2, 26]));