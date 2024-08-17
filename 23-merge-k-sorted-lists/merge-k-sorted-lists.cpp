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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) {
            return nullptr;
        }

        while (lists.size() > 1) {
            vector<ListNode*> temp;
            for (int i = 0; i < lists.size(); i += 2) {
                ListNode* first = lists[i];   
                ListNode* second = (i+1 < lists.size()) ? lists[i+1] : nullptr;
                temp.push_back(merge(first,second));
            }
            lists = temp;
        }

        return lists[0];
    }

private:
    ListNode* merge(ListNode* first, ListNode* second) {
        ListNode* ans = new ListNode();
        ListNode* dummy = ans;

        while (first != nullptr && second != nullptr){
            if (first->val > second->val) {
                ans->next = new ListNode(second->val);
                ans = ans->next;
                second = second->next;
            } else {
                ans->next = new ListNode(first->val);
                ans = ans->next;
                first = first->next;
            }
        }

        if (first != nullptr) {
            ans->next = first;
        }
        if (second != nullptr) {
            ans->next = second;
        }

        return dummy->next;
    }
};  