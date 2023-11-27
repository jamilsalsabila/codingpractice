var addStrings = function (num1, num2) {
    let l1 = num1.length - 1;
    let l2 = num2.length - 1;
    let n1 = 0;
    let n2 = 0;
    let result = [];
    let carry = 0;
    let add = 0;

    while (l1 > -1 || l2 > -1) {
        n1 = (l1 === -1) ? 0 : num1.charCodeAt(l1) - 48;
        n2 = (l2 === -1) ? 0 : num2.charCodeAt(l2) - 48;

        add = n1 + n2 + carry;

        if (add / 10 >= 1) {
            result.push(String.fromCharCode((add % 10) + 48));
            carry = 1;
        } else {
            result.push(String.fromCharCode(add + 48));
        }

        l1 = l1 - 1;
        l2 = l2 - 1;

        console.log(l1, l2);
    }

    for (let i = 0; i < Math.floor(result.length / 2); i++) {
        let temp = result[i];
        result[i] = result[result.length - 1 - i];
        result[result.length - 1 - i] = temp;
    }

    return result.reduce((a, b) => a + b);
};

console.log(addStrings("11", "123"));