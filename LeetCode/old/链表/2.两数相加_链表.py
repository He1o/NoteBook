'''
题目描述
给你两个非空的链表，表示两个非负的整数。
它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
'''

from Def import LinkedList
from Def import timer

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = LinkedList.Node()
        temphead = head
        givenum = 0
        while l1 or l2 or givenum:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            total = num1 + num2 + givenum
            temphead.next = LinkedList.Node(total % 10)
            givenum = total // 10
            temphead = temphead.next
            if l1 : l1 = l1.next 
            if l2 : l2 = l2.next 
        return head.next

'''
1. if else条件表达式来对不符合的变量赋值0，而不是判断之后修改计算公式，
2. 链表可以正序也可以倒序，把当前地址作为下一个的next，
head = None
head = LinkedList.Node(x, head)
|——————————|       |——————————|       |——————————|       |——————————|
|         ←|-------|         ←|-------|         ←|-------|          |
|——————————|       |——————————|       |——————————|       |——————————|
      ↑（指针最后位置）             ←-------                 ↑（指针初始）

temp = head = LinkedList.Node(0, None)
temp.next = LinkedList.Node(x,  None)
|——————————|       |——————————|       |——————————|       |——————————|
|         ←|-------|         ←|-------|         ←|-------|          |
|——————————|       |——————————|       |——————————|       |——————————|
      ↑（head指针初始位置不变）     
      ↑（temp指针从左到右）      -------→                    ↑（temp指针最后）
3. head指向的第一个Node值为0，那就返回第二项不就行了，head.next

'''

L1 = [9,9,9,9,9,9,9]
L2 = [9,9,9,9]
L1 = LinkedList.list_to_Linked(L1)
L2 = LinkedList.list_to_Linked(L2)

S = Solution()   
re = LinkedList.linked_to_list(S.addTwoNumbers(L1, L2))
print(re)