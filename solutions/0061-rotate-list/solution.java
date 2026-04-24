class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        // Base case: empty list, single node, or no rotation needed
        if (head == null || head.next == null || k == 0) return head;

        // 1. Calculate the length and find the actual tail node
        ListNode oldTail = head;
        int length = 1;
        while (oldTail.next != null) { // Fix: Stop AT the last node, not after it
            oldTail = oldTail.next;
            length++;
        }

        // 2. Connect the tail to the head to form a temporary cycle
        oldTail.next = head;

        // 3. Find the new tail: (length - k % length - 1) steps from the head
        k = k % length;
        int stepsToNewTail = length - k;

        ListNode newTail = head;
        // Since we start at head, we need to move (stepsToNewTail - 1) times
        for (int i = 1; i < stepsToNewTail; i++) {
            newTail = newTail.next;
        }

        // 4. Break the cycle
        ListNode newHead = newTail.next;
        newTail.next = null;

        return newHead;
    }
}

