/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // reverse linked list or use stack
        ListNode* r1 = reverse(l1);
        ListNode* r2 = reverse(l2);
        
        // then do the adding of two LLs
        ListNode* dummy = new ListNode();
        ListNode* ans = dummy;
        int carry = 0;

        while (r1 != nullptr || r2 != nullptr || carry != 0) {
            int firstDigit = (r1 != nullptr) ? r1->val : 0;
            int secondDigit = (r2 != nullptr) ? r2->val : 0;

            int sum = firstDigit + secondDigit + carry;
            int val = sum % 10;
            carry = sum / 10;

            ans->next = new ListNode(val);
            ans = ans->next;

            r1 = (r1 != nullptr) ? r1->next : nullptr;
            r2 = (r2 != nullptr) ? r2->next : nullptr;
        }

        // Reverse the resultant linked list back to original order
        ListNode* result = reverse(dummy->next);

        return result;
    }

private:
    ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
};