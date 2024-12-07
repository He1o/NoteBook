'''
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 
示例 1：
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

示例 2：
输入：head = [5], left = 1, right = 1
输出：[5]

'''
from Def import LinkedList

class Solution:
    def reverseBetween(self, head, left, right):
        def reverse(head, tail):
            last = tail.next
            curr = head.next
            head.next = last
            while head != tail:
                temp = curr.next
                curr.next = head
                head = curr
                curr = temp
            return tail       
        
        pre = dummy = LinkedList.Node(0, head)
        le = ri = head
        left -= 1
        right -=1

        while left or right:
            if left > 0:
                le = le.next
                left -= 1
                pre = pre.next
            if right > 0:
                ri = ri.next
                right -= 1
        pre.next = reverse(le, ri)

        return dummy.next

    # 头插法
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next



L1 = [1, 2, 3, 4, 5]
L1 = LinkedList.list_to_Linked(L1)

S = Solution()   
re = LinkedList.linked_to_list(S.reverseBetween(L1, 2, 4))
print(re)
                    




