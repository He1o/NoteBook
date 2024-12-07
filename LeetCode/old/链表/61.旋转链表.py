'''
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

示例 2：
输入：head = [0,1,2], k = 4
输出：[2,0,1]
'''

from Def import LinkedList

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None
        num = 0
        dummy = LinkedList.Node(0, head)
        
        while True:
            num += 1
            if not head.next:
                head.next = dummy.next
                k = (num - k % num) / num
                while k:
                    k -= 1
                    head = head.next
                temp = head.next
                head.next = None
                return temp

            head = head.next
            

        




        
