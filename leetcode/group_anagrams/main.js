/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
    let d = {};
    strs.forEach((str) => {
        let c = str.split('').sort().join('');

        if (!d.hasOwnProperty(c)) {
            d[c] = [];
        }
        d[c].push(str);
    });
    let result = [];
    for (let key in d) {
        result.push(d[key]);
    }
    return result;
};