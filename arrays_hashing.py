class TwoSum:
    """
    Given an integer array nums and an integer target, find indices i and j such that nums[i] + nums[j] == target and i != j.
    Assume that every input has exactly one pair of indices i and j that fulfill this condition.
    Return the pair of indices with the smaller index first.

    Example 1:
    Input: nums = [1, 2, 3, 4], target = 5
    Output: [0, 3]
    Explanation: nums[0] + nums[3] == 5, so we return [0, 3].

    Example 2:
    Input: nums = [0, -1, 2, -3, 1], target = -2
    Output: [1, 3]
    """
    def twoSum(self, nums: list, target: int) -> list:
        # Dictionary to store elements based on index
        store_dict = {}

        for i, num in enumerate(nums):
            diff = target - num

            # if difference is found in dict, return the actual number, if not store it based on index
            if diff in store_dict:
                return [store_dict[diff], i]
            
            store_dict[num] = i

# obj1 = TwoSum()
# print(obj1.twoSum([0, -1, 2, -3, 1], -2))
# print(obj1.twoSum([1, 2, 3, 4], 5))


class Anagram:
    """
    Given two strings s and t, determine whether t is an anagram of s. Return true if they are anagrams, and false otherwise.
    An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.
    Example 1:
    Input: s = "god", t = "dog"
    Output: true
    Example 2:
    Input: s = "can", t = "pan"
    Output: false
    """
    def isAnagram(self, s: str, t: str) -> bool:
        for index, char in enumerate(s):
            if char != t[-index-1]:
                return False       
        return True
    
# obj2 = Anagram()
# print(obj2.isAnagram("god", "dog"))
# print(obj2.isAnagram("can", "pan"))


class HasDuplicate:
    """
    Given an integer array nums, determine whether any element appears more than once. Return true if a duplicate exists, and false otherwise.
    Example 1:
    Input: nums = [1, 1, 2, 3]
    Output: true
    Example 2:
    Input: nums = [1, 2, 3, 4]
    Output: false
    """
    def hasDuplicate(self, nums: list) -> bool:
        countDict = {}

        for num in nums:
            if num in countDict:
                 return True
            countDict[num] = 1

        return False
    
# obj3 = HasDuplicate()
# print(obj3.hasDuplicate([1, 1, 2, 3]))
# print(obj3.hasDuplicate([1, 2, 3, 4]))

class ProductExceptSelf:
    """
    Given an integer array nums, return an array output where output[i] is the product of all elements in nums except for nums[i].
    Each product is guaranteed to fit within a 32-bit integer.
    Solve this in O(n) time complexity without using the division operation.

    Example 1:
    Input: nums = [1, 3, 5, 7]
    Output: [105, 35, 21, 15]

    Example 2:
    Input: nums = [2, 4, 6, 8]
    Output: [192, 96, 64, 48]
    """
    def productExceptSelf(self, nums: list) -> list:
        # Initialize result array with all 1s
        result = [1] * len(nums)
        
        # Left to Right: Compute the running product of elements before each index and store it in the result array.
        prefix = 1 
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Right to Left: Compute the running product of elements after each index and multiply it with the corresponding value in result.
        postFix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postFix
            postFix *= nums[i]

        return result


# obj4 = ProductExceptSelf()
# print(obj4.productExceptSelf([1, 3, 5, 7]))
# print(obj4.productExceptSelf([2, 4, 6, 8]))

class GroupAnagrams:
    """
    You are given an array of strings strs. Your task is to group all the anagrams together into separate sublists. The order of the groups in the output does not matter.
    Definition: An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

    Example 1:
    Input: strs = ["race", "care", "acre", "hello", "world", "dworl"]
    Output: [["race", "care", "acre"], ["hello"], ["world", "dworl"]]
    Explanation:
    "race", "care", and "acre" form one group of anagrams.
    "hello" has no anagrams in the list.
    "world" and "dworl" are anagrams of each other.

    Example 2:
    Input: strs = ["a"]
    Output: [["a"]]

    Example 3:
    Input: strs = ["", "", "a", "b", "ab", "ba"]
    Output: [["", ""], ["a"], ["b"], ["ab", "ba"]]
    """
    def groupAnagrams(self, strs: list) -> list[list[str]]:
        # Use defaultdict to automatically initialize empty lists
        result = dict()

        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1

             # Use tuple of counts as key since lists can't be dictionary keys
            if tuple(count) not in result:
                result[tuple(count)] = [str]
            else:
                result[tuple(count)].append(str)

        return list(result.values())
      
# obj5 = GroupAnagrams()
# print(obj5.groupAnagrams(["race", "care", "acre", "hello", "world", "dworl"]))
# print(obj5.groupAnagrams(["a"]))
# print(obj5.groupAnagrams(["", "", "a", "b", "ab", "ba"]))


class EncodeDecode:
    """
    Develop an algorithm to convert a list of strings into a single encoded string, such that it can be decoded back into the original list of strings without any loss of information.
    Implement encode and decode functions:
    encode: Takes a list of strings and returns a single encoded string.
    decode: Takes an encoded string and returns the original list of strings.

    Example 1:
    Input: ["tech", "prep", "is", "op"]
    Output: ["tech", "prep", "is", "op"]

    Example 2:
    Input: ["how", "you", "?", "doing"]
    Output: ["how", "you", "?", "doing"]
    """
    def encode(self, strs: list[str]) -> str:
        # Encode each string with its length followed by delimiter
        encoded_strs = []
        for s in strs:
            encoded_strs.append(str(len(s)) + '#' + s)
        return ''.join(encoded_strs)
    
    def decode(self, s: str) -> list[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            # Find the position of the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1

            # Extract length and move past '#'
            strLen = int(s[i:j])
            j += 1

            # Extract the string using slicing
            decoded_strs.append(s[j:j+strLen])

            # Move index to the next encoded string
            i = j + strLen

        return decoded_strs

            
obj6 = EncodeDecode()
print(obj6.encode(["tech", "prep", "is", "op"]))
print(obj6.decode(obj6.encode(["tech", "prep", "is", "op"])))

print(obj6.encode(["how", "you", "?", "doing"]))
print(obj6.decode(obj6.encode(["how", "you", "?", "doing"])))
