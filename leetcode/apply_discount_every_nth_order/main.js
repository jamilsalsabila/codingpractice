/**
 * @param {number} n
 * @param {number} discount
 * @param {number[]} products
 * @param {number[]} prices
 */
var Cashier = function (n, discount, products, prices) {
    this.n = n;
    this.discount = discount;
    this.products = products;
    this.prices = prices;

    this.productsXprices = {};
    this.products.forEach((product, i) => this.productsXprices[product] = this.prices[i]);
    this.nCustomer = 1;
};

/** 
 * @param {number[]} product 
 * @param {number[]} amount
 * @return {number}
 */
Cashier.prototype.getBill = function (product, amount) {
    let total = 0;

    for (let i = 0; i < product.length; i++) {
        total += this.productsXprices[product[i]] * amount[i];
    }
    if ((this.nCustomer % this.n) === 0) {
        total = total * ((100 - this.discount) / 100);
    }

    this.nCustomer += 1;
    return total.toFixed(5);
};

/** 
 * Your Cashier object will be instantiated and called as such:
 * var obj = new Cashier(n, discount, products, prices)
 * var param_1 = obj.getBill(product,amount)
 */

var obj = new Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100]);
console.log(obj.getBill([1, 2], [1, 2]));
console.log(obj.getBill([3, 7], [10, 10]));
console.log(obj.getBill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]));
console.log(obj.getBill([4], [10]));
console.log(obj.getBill([7, 3], [10, 10]));
console.log(obj.getBill([7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7]));