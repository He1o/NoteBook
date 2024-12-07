'''
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]

'''


from Def import LinkedList


class Solution:

    # 顺序合并
    def mergeKLists(self, lists):
        '''
        时间复杂度  O(k^2 * n) 假设每个链表长度n，第一次合并后ans长度为n，诶二次为2n， 第i次为i*n
                第i次合并时间为O(n+(i-1)n)=O(i*n) 总时间O(∑i=1-k(i*n))=(1+k)*k/2 = O(k^2 * n) 
        空间复杂度  O(1)
        '''
        if not lists:
            return None
        l1 = lists[0]
        for l2 in lists[1:]:
            l1 = self.mergeTwoLists(l1,l2)

        return l1
    
    
    # 分治算法
    def mergeKLists(self, lists):
        '''
        时间复杂度  第一轮合并k/2组链表，每一组时间代价是O(2n),第二轮k/4，时间代价O(4n)
                    总的时间代价O(∑i=1-∞ k/2^i * 2^i *n) = O(kn*logk)
        空间复杂度  递归会用到O(logk)空间代价的栈空间
        '''
        if not lists:
            return None

        def dc(i ,j):
            if i == j:
                return lists[i]
            mid = (i + j) // 2
            l1 = dc(i, mid)
            l2 = dc(mid + 1, j)
            return self.mergeTwoLists(l1, l2)
        return dc(0, len(lists) - 1)

    def mergeTwoLists(self, l1, l2):
        if l2 == None:
            return l1
        elif l1 == None:
            return l2

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
'''
是分治和单纯的合并，两个递归系统一个套在另一个的底层

1 2 3 4 5 6 7 8
↑             ↑
1 2 3 4|5 6 7 8
↑     ↑ ↑     ↑
1 2|3 4|5 6|7 8
↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑


'''


L1 = [1,4,5]
L2 = [1,3,4]
L3 = [2,6]
L1 = LinkedList.list_to_Linked(L1)
L2 = LinkedList.list_to_Linked(L2)
L3 = LinkedList.list_to_Linked(L3)
l = [L1, L2, L3]
S = Solution()   
# with timer.timer('time'):
re = LinkedList.linked_to_list(S.mergeKLists(l))
print(re)