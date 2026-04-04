/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }

        // Start with the first list as our initial merged result
        ListNode mergedResult = lists[0];

        // Iteratively merge the current result with the next list in the array
        for (int i = 1; i < lists.length; i++) {
            mergedResult = mergeTwoLists(mergedResult, lists[i]);
        }

        return mergedResult;
    }

    // Helper method to merge two sorted linked lists using two pointers (Merge Sort logic)
    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Dummy node helps handle the head of the new list easily
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
        }

        // If one list is exhausted, attach the remainder of the other list
        if (l1 != null) {
            current.next = l1;
        } else {
            current.next = l2;
        }

        return dummy.next;
    }
}

