/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    let m = {
        '(': ')',
        '{': '}',
        '[': ']',
    };
    let st = [];
    let c = '';

    for (let i = 0; i < s.length; i++) {
        switch (s[i]) {
            case '[':
                st.push(s[i]);
                break;
            case '(':
                st.push(s[i]);
                break;
            case '{':
                st.push(s[i]);
                break;
            case ']':
                c = st.pop();
                if (m[c] !== ']') {
                    return false;
                }
                break;
            case ')':
                c = st.pop();
                if (m[c] !== ')') {
                    return false;
                }
                break;
            case '}':
                c = st.pop();
                if (m[c] !== '}') {
                    return false;
                }
                break;
        }
    }
    if (st.length > 0) {
        return false;
    }
    return true;
};

console.log(isValid("()"));
console.log(isValid("(){}[]"));
console.log(isValid("(]"));
console.log(isValid("(((([]))))"));