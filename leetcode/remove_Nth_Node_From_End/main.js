
// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/*
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
    let h = new ListNode()
    h.next = head;

    let remove = function (h, n) {
        if (h === null) {
            return n - 1;
        }
        let r = remove(h.next, n);
        if (r > -1) {
            return r - 1;
        } else if (r === -1) {
            let p = h.next;
            h.next = p.next;
            p.next = null;
        }
        return r - 1;
    }
    let H = remove(h, n)

    return h.next
};