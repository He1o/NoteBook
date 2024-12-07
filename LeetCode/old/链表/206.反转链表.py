'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 
示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]
'''
from Def import LinkedList

class Solution:
    # 迭代
    def reverseList1(self, head):
        dummy = LinkedList.Node(0, None)
        dummy.next = head
        pre = head
        tail = head.next
        while tail:
            dummy.next = tail
            pre.next = tail.next
            tail.next = head
            
            head = tail
            tail = pre.next
        return dummy.next

    # 迭代改进
    def reverseList1(self, head):
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre

            pre = cur
            cur = temp
        return pre

    #错误递归
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        temp = self.reverseList(head.next)
        tail = temp
        while tail.next:
            tail = tail.next
        tail.next = head
        head.next = None

        return temp
        
    #递归
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp

'''
递归的时候无需从temp抵达末尾，因为head指向的下一个就是末尾，这一点很巧妙


|——————————|       |——————————|       |——————————|       |——————————|
|    1     |-------|→   2     |-------|→   3     |-------|→   4     |------→None
|——————————|       |——————————|       |——————————|       |——————————|
                                           ↑                  ↑
                                          head               temp

                                            ↗   →    →    →    →    →    ↘
                                           ↑                                 ↓
|——————————|       |——————————|       |——————————|       |——————————|
|    1     |-------|→   2     |-------|→   3    ←|-------|    4     |------→None
|——————————|       |——————————|       |——————————|       |——————————|
                        ↑                                     ↑
                       head                                  temp
'''


L1 = [1,2,4,6]
L1 = LinkedList.list_to_Linked(L1)

S = Solution()   
re = LinkedList.linked_to_list(S.reverseList(L1))
print(re)