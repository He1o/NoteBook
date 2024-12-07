'''
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。

返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,1,2]
输出：[1,2]

示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]
'''

from Def import LinkedList


class Solution:
    def deleteDuplicates(self, head):
        pre = head
        curr = head.next
        while curr:
            if curr.val == pre.val:
                pre.next = curr.next
            else:
                pre = pre.next
            curr = curr.next
        return head

    # 改进
    def deleteDuplicates(self, head):
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
