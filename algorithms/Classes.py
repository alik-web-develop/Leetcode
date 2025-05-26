# Решение Two Sum
class TwoSum:
    def twoSum(self, nums, target):
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []

# Решение Valid Parentheses
class ValidParentheses:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

# Решение Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseLinkedList:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev

# Решение Merge Two Sorted Lists
class MergeSortedLists:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy.next

# Решение Binary Search
class BinarySearch:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# Решение Climbing Stairs
class ClimbingStairs:
    def climbStairs(self, n):
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# Решение Valid Palindrome
class ValidPalindrome:
    def isPalindrome(self, s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]

# Решение Maximum Subarray
class MaximumSubarray:
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

# Решение Single Number
class SingleNumber:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

# Решение Move Zeroes
class MoveZeroes:
    def moveZeroes(self, nums):
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1

# Примеры использования:
if __name__ == "__main__":
    # Two Sum
    two_sum = TwoSum()
    print(two_sum.twoSum([2, 7, 11, 15], 9))  # [0, 1]

    # Valid Parentheses
    valid_parens = ValidParentheses()
    print(valid_parens.isValid("()[]{}"))  # True

    # Binary Search
    binary_search = BinarySearch()
    print(binary_search.search([-1, 0, 3, 5, 9, 12], 9))  # 4

    # Climbing Stairs
    climbing = ClimbingStairs()
    print(climbing.climbStairs(3))  # 3

    # Valid Palindrome
    palindrome = ValidPalindrome()
    print(palindrome.isPalindrome("A man, a plan, a canal: Panama"))  # True
