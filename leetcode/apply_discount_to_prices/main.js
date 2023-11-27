/**
 * @param {string} sentence
 * @param {number} discount
 * @return {string}
 */
var discountPrices = function (sentence, discount) {
    let token = sentence.split(/\s+/);
    // console.log(token);
    let price = token.filter((t) => t.match(/^\$\d+$/));
    // console.log(price);
    let num = price.map((p) => parseFloat(p.match(/\d+/)[0]));
    // console.log(num);
    let disc = num.map((n) => `$${(n - (n * discount / 100)).toFixed(2)}`);
    // console.log(disc);

    let j = 0;
    let curr = price[j];
    for (let i = 0; i < token.length; i++) {
        if (token[i] === curr) {
            token[i] = disc[j];
            j = j + 1;
            if (j === disc.length) {
                break;
            }
            curr = price[j];
        }
    }
    // console.log(token);
    return token.join(' ');
};

console.log(discountPrices("duew$11mengf $8 $1", 7));
console.log(discountPrices("there are $1 $2 and 5$ candies in the shop", 50));
console.log(discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100));