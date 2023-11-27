// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    let carry = 0;
    let result = new ListNode(0);
    let pointer = result;

    while (l1 || l2) {
        if (l1) {
            pointer.val += (carry + l1.val);
            carry = 0;
            l1 = l1.next;
        }

        if (l2) {
            pointer.val += (l2.val + carry);
            carry = 0;
            l2 = l2.next;
        }

        if ((pointer.val / 10) >= 1) {
            pointer.val = pointer.val % 10;
            carry = 1;
        }

        if (l1 || l2) {
            pointer.next = new ListNode(0);
            pointer = pointer.next;
        }
    }

    if (carry === 1) {
        pointer.next = new ListNode(1);
        pointer = pointer.next;
    }

    return result;
};

let L1 = new ListNode(9, new ListNode(9, new ListNode(9)));
let L2 = new ListNode(1, new ListNode(1, new ListNode(1)));

console.log(addTwoNumbers(L1, L2));
