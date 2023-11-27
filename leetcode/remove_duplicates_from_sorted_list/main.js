
// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
    let p = head;
    while (p !== null) {
        while (p.next !== null && p.val === p.next.val) {
            let tmp = p.next;
            p.next = tmp.next;
            tmp.next = null;
        }
        p = p.next;
    }
    return head;
};