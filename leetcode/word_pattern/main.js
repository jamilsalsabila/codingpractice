/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function (pattern, s) {
    let pattern_s = pattern.split('');
    let s_s = s.split(' ');
    let d_p = {};
    let d_s = {};

    if (s_s.length !== pattern_s.length) return false;

    for (let i = 0; i < pattern_s.length; i++) {
        if (!d_p[pattern_s[i]] && !d_s[s_s[i]]) {
            d_p[pattern_s[i]] = s_s[i];
            d_s[s_s[i]] = pattern_s[i];
        }
        else if (d_p[pattern_s[i]] || d_s[s_s[i]]) {
            if (d_p[pattern_s[i]] !== s_s[i]) return false;
            if (d_s[s_s[i]] !== pattern_s[i]) return false;
        }
    }
    return true;
};

console.log(wordPattern("abba", "dog cat cat dog"));
