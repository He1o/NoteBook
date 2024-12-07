'''
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

示例 1：
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]

示例 2：
输入：head = [2,1], x = 2
输出：[1,2]

'''

from Def import LinkedList

class Solution:
    def partition(self, head, x):
        large = LinkedList.Node(0, None)
        little = LinkedList.Node(0, head)

        currli = little
        currla = large
        while currli.next:
            if currli.next.val >= x:
                currla.next = currli.next
                
                currli.next = currli.next.next

                currla = currla.next
                currla.next = None

            else:
                currli = currli.next
        currli.next = large.next
        return little.next

        
L1 = [1,4,3,2,5,2]
L1 = LinkedList.list_to_Linked(L1)

S = Solution()   
re = LinkedList.linked_to_list(S.partition(L1, 3))
print(re)  
