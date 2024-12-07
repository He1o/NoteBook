'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]
'''
from Def import LinkedList

class Solution:
    #迭代
    def swapPairs1(self, head):
        dummy = LinkedList.Node(0, None)
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummy.next


    #递归
    def swapPairs(self, head):
        if not head or not head.next:
            return head
            
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp

'''
可以通过递归的方式实现两两交换链表中的节点。

递归的终止条件是链表中没有节点，或者链表中只有一个节点，此时无法进行交换。

如果链表中至少有两个节点，则在两两交换链表中的节点之后，
原始链表的头节点变成新的链表的第二个节点，原始链表的第二个节点变成新的链表的头节点。
链表中的其余节点的两两交换可以递归地实现。在对链表中的其余节点递归地两两交换之后，
更新节点之间的指针关系，即可完成整个链表的两两交换。
'''

L1 = [1,2,4,6]
L1 = LinkedList.list_to_Linked(L1)

S = Solution()   
re = LinkedList.linked_to_list(S.swapPairs(L1))
print(re)

