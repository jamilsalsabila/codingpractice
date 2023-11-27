/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
    let m = s.match(/^\s*([-+]?\d+)[^a-zA-Z]*\s*/);
    if (m === null) return 0;
    let ns = m[1];
    let neg = (ns[0] === '-') ? true : false;
    let b = neg ? ns.slice(1) : ns;
    b = (b[0] === '+') ? b.slice(1) : b;
    let c = 0;
    for (let i = 0; i < b.length; i++) {
        c += (b.charCodeAt(i) - 48) * Math.pow(10, b.length - 1 - i);
    }
    c = (neg) ? c * -1 : c;
    if (c <= Math.pow(-2, 31)) return Math.pow(-2, 31);
    if (c >= (Math.pow(2, 31) - 1)) return Math.pow(2, 31) - 1;
    return c;

};