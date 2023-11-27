/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
    s = s.toLowerCase();
    s = s.replace(/[\W\s]+/ig, '');
    for (let i = 0; i < Math.floor(s.length / 2); i++)
        if (s[i] !== s[s.length - 1 - i])
            return false
    return true;
};

console.log(isPalindrome("A man, a plan, a canal: Panama"));