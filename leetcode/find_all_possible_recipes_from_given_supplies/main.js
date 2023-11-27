/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function (recipes, ingredients, supplies) {
    let d = {};
    let result = {};
    for (let i = 0; i < recipes.length; i++) {
        if (!d[recipes[i]]) d[recipes[i]] = ingredients[i];
    }
    for (let k in d) {
        let c = d[k].length;
        for (let r of d[k]) {
            if (supplies.findIndex(i => i === r) > -1) c--;
            else {
                let tmp = [];
                while (d[r])
            }
        }
        if (c === 0) result[k] = true;
    }
    return Object.keys(result);

};

console.log(findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]));