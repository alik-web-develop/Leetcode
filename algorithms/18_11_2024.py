# # # 151. Reverse Words in a String
# # # Given an input string s, reverse the order of the words.
# # # A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# # # Return a string of the words in reverse order concatenated by a single space.
# # # Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# # # x = "   Пример строки с пробелами   "
# # # def reverse_words(text):
# # #     result = []
# # #     [result.append(i) for i in text.split() if i]
# # #     result = result[::-1]
# # #     return (" ".join(result))
# # # print(reverse_words("  hello world  "))
# # # 92. Reverse Linked List II
# # # Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# # # x = [1,2,3,4,5,6,7,8,9,10]
# # # def reverse_linked(arr,left,right):
# # #     else:

# # # вот тут литкод мой код не принял так как к нам оказывается приходит не просто list а ListNode это то ещё проблема так как там нету индексации типо вы не можете использовать element[left:right] из за этого пришлось голову морочить вот короче код который литкод принял
# # class Solution:
# #     def reverseBetween(self, head, left: int, right: int):
# #         dummy = ListNode(0)
# #         dummy.next = head
# #         prev = dummy
# #         current = prev.next
        
# #         for _ in range(right - left):
# #             temp = current.next
# #             current.next = temp.next
# #             temp.next = prev.next
# #             prev.next = temp
        
# #         if len(s) != len(t):
# #             return False