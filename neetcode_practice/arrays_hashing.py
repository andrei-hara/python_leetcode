class HasDuplicate:
    """
    Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

    Example 1:

    Input: nums = [1, 2, 3, 3]

    Output: true

    Example 2:

    Input: nums = [1, 2, 3, 4]

    Output: false
    """
    def hasDuplicate(self, nums: list[int]) -> bool:
        keyDict = {}
        for num in nums:
            if num not in keyDict:
                keyDict[num] = 1
            else:
                return True
            
        return False
    
# obj1 = HasDuplicate()
# print(obj1.hasDuplicate([1, 2, 3, 3]))
# print(obj1.hasDuplicate([1, 2, 3, 4]))

class Anagram:
    """
    Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

    Example 1:

    Input: s = "racecar", t = "carrace"

    Output: true
    Example 2:

    Input: s = "jar", t = "jam"

    Output: false
    Constraints:

    s and t consist of lowercase English letters.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}

        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1
            if t[i] not in dict_t:
                dict_t[t[i]] = 1
            else:
                dict_t[t[i]] += 1
        
        if dict_s != dict_t:
            return False
        else:
            return True

obj2 = Anagram()
print(obj2.isAnagram("racecar", "carrace"))
print(obj2.isAnagram("jar", "jam"))


class TwoSum:
    """
    Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

    You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

    Return the answer with the smaller index first.

    Example 1:

    Input: 
    nums = [3,4,5,6], target = 7

    Output: [0,1]
    Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

    Example 2:

    Input: nums = [4,5,6], target = 10

    Output: [0,2]
    Example 3:

    Input: nums = [5,5], target = 10

    Output: [0,1]
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store elements based on index
        store_dict = {}

        for i, num in enumerate(nums):
            diff = target - num

             # if difference is found in dict, return the index of the numbers, if not store it based on index
            if diff in store_dict:
                return [store_dict[diff], i]
            
            store_dict[num] = i

    
obj3 = TwoSum()
print(obj3.twoSum(nums = [3,4,5,6], target = 7))
print(obj3.twoSum(nums = [4,5,6], target = 10))
print(obj3.twoSum(nums = [5,5], target = 10))