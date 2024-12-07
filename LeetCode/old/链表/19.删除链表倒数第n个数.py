'''给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？


示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]
'''

from Def import LinkedList

class Solution:
    # 方法一 计算链表长度
    def removeNthFromEnd2(self, head, n):
        def getlength(head):
            length = 0
            temp_head = head
            while temp_head:
                temp_head = temp_head.next
                length = length + 1
            return length
            
        dummy = LinkedList.Node(0, head)
        length = getlength(head)
        temp = dummy
        for _ in range(length - n):
            temp = temp.next
        temp.next = temp.next.next

        return dummy.next
    
    #方法二  栈
    def removeNthFromEnd3(self, head, n):
        dummy = LinkedList.Node(0, head)
        stack = []
        temp = dummy
        while temp:
            stack.append(temp)
            temp = temp.next

        for _ in range(n):
            stack.pop()
        stack[-1].next = stack[-1].next.next

        return dummy.next


    #方法三  双指针
    def removeNthFromEnd(self, head, n):
        dummy = LinkedList.Node(0, head)
        first = head
        second = dummy
        for _ in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
'''
哑结点
在对链表进行操作时，一种常用的技巧是添加一个哑节点（dummy node），
它的next指针指向链表的头节点。这样一来，我们就不需要对头节点进行特殊的判断了。

例如，在本题中，如果我们要删除节点 yy，我们需要知道节点 yy 的前驱节点 xx，
并将 xx 的指针指向 yy 的后继节点。但由于头节点不存在前驱节点，
因此我们需要在删除头节点时进行特殊判断。但如果我们添加了哑节点，那么头
的前驱节点就是哑节点本身，此时我们就只需要考虑通用的情况即可。

|——————————|       |——————————|       |——————————|       |——————————|       |——————————|
|         ←|-------|    1    ←|-------|    2    ←|-------|    3    ←|-------|    4    ←|-------None
|——————————|       |——————————|       |——————————|       |——————————|       |——————————|
    dummy
    ↑second           n = 1               ↑first


|——————————|       |——————————|       |——————————|       |——————————|       |——————————|
|         ←|-------|    1    ←|-------|    2    ←|-------|    3    ←|-------|    4    ←|-------None
|——————————|       |——————————|       |——————————|       |——————————|       |——————————|
                                                              ↑second           n = 1           ↑first
'''
L1 = [1, 2]
L1 = LinkedList.list_to_Linked(L1)

S = Solution()   
# with timer.timer('time'):
re = LinkedList.linked_to_list(S.removeNthFromEnd(L1, 2)) 

print(re)