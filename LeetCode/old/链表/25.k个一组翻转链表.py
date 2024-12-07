'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

示例 2：
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

示例 3：
输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]

示例 4：
输入：head = [1], k = 1
输出：[1]
'''
from Def import LinkedList

class Solution:
    # 原版
    def reverseKGroup1(self, head, k):
        def reverseList(head, tail):
            pre = tail
            dummy = head
            while head != tail:
                temp = head.next
                head.next = pre

                pre = head
                head = temp
            
            return pre, dummy

        n = 1
        dummy = LinkedList.Node(0, None)
        dummy.next = head
        temp_head = tail = head
        first = True
        origin = head
        while tail:
            if n != 1 and n == k:
                newhead, newtail = reverseList(temp_head, tail.next)
                dummy.next = newhead
                if first:
                    origin = newhead
                    first = False

                dummy = newtail
                temp_head = tail = newtail.next
                n = 1
            if tail:
                tail = tail.next
            n += 1

        return origin

    # 第二版
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        def reverse(head, tail):
            dummy = head
            temp = head.next
            head.next = tail.next
            while head != tail:
                head2 = temp
                temp = temp.next
                head2.next = head
                head = head2
            return tail, dummy
            
        dummy = LinkedList.Node(0, head)
        tail = dummy
        head = dummy
        n = 0
        while tail:
            if n == k:
                newhead, tail = reverse(head.next, tail)
                head.next = newhead
                head = tail
                n = 0
            tail = tail.next
            n += 1
        return dummy.next

        
    # 修改
    def reverseKGroup1(self, head, k):
        def reverseList(head, tail):
            pre = tail
            dummy = head
            while head != tail:
                temp = head.next
                head.next = pre

                pre = head
                head = temp
            return pre, dummy

        dummy = LinkedList.Node(0, None)
        dummy.next = head
        pre = dummy
        while head:

            tail = pre
            for i in range(k):
                if tail.next != None:
                    tail = tail.next
                else:
                    return dummy.next
                
            newhead, newtail = reverseList(head, tail.next)
            pre.next = newhead

            tail = pre = newtail
            head = newtail.next

        return dummy.next




'''
分两部分
注意接口指针的位置
初始的pre会移动，那在移动开始前把pre指向另一个指针不就行了
开始想的创建两个node，没有意义
对pre.next赋值将pre指向正确的head
改变pre的时候，才会丢失正确的head
那么在一开始dummy=pre即可解决返回问题


    0      1      2     3     4     5     None
    ↑      ↑        
   pre    head 
   dummy
   tail

    0      1      2     3     4     5     None
    ↑      ↑      ↑
   pre    head   tail
   dummy

           ↑ →  →  →  → ↓
    0   →  1   ←  2     3     4     5     None
    ↑      ↑      ↑
   pre    head   tail
   dummy  newtail newhead

    0   →  2   →  1   →  3     4     5     None
    ↑      ↑      ↑
   pre    tail    head   
   dummy  newhead newtail 

    0   →  2   →  1   →  3     4     5     None
    ↑      ↑      ↑      ↑
                  pre    head
   dummy          tail 

    0   →  2   →  1   →  4  →  3     5     None
    ↑      ↑      ↑      ↑     ↑     ↑
                               pre    head
   dummy                       tail 

    0   →  2   →  1   →  4  →  3     5     None
    ↑      ↑      ↑      ↑     ↑     ↑
                               pre    head
   dummy                                    tail 
'''

L1 = [1, 2, 3, 4, 5]
L1 = LinkedList.list_to_Linked(L1)

S = Solution()   
re = LinkedList.linked_to_list(S.reverseKGroup(L1, 2))
print(re)
            