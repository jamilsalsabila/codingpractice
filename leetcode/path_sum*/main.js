
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */
let preorder = function (p, targetSum, current) {
    if (p === null) {
        if (targetSum === current) return true;
        else return false;
    }
    current = current + p.val;
    let L = preorder(p.left, targetSum, current);
    if (L) {
        return L;
    }
    let R = preorder(p.right, targetSum, current);
    if (R) {
        return R;
    }
}
var hasPathSum = function (root, targetSum) {
    let current = 0;
    let A = preorder(root, targetSum, current);
    return A;
};