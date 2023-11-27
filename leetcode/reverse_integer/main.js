/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    let power = 0;
    let negative = false;

    if (x < 0) {
        negative = true;
        x = x * -1;
    }

    let copy_x = x;

    while (copy_x >= 1) {
        power += 1;
        copy_x = Math.floor(copy_x / 10);
    }

    let result = 0;

    while (power >= 1) {
        result += (x % 10) * Math.pow(10, power - 1);
        x = Math.floor(x / 10);
        power -= 1;
    }

    if (negative)
        result = result * -1

    if (result === Math.pow(-2, 31) || result === Math.pow(2, 31) - 1)
        return 0;

    return result;
};

console.log(reverse(1));
console.log(reverse(120));
console.log(reverse(-123));
