class MinSortedArray:
    """
    You are provided with an array nums of length n, which was initially sorted in ascending order. This array has been rotated between 1 and n times. For instance, consider the sorted array nums = [1, 2, 3, 4, 5, 6]:
    After rotating it 4 times, it becomes [3, 4, 5, 6, 1, 2].
    Rotating it 6 times results in [1, 2, 3, 4, 5, 6], which is the original array.
    Rotating the array k times moves the last k elements to the front of the array. Your task is to find the smallest element in this rotated array nums.
    Note: All elements in nums are unique. While a straightforward solution with a time complexity of O(n) exists, aim to implement an algorithm that achieves O(log n) time complexity.
    
    Example 1:
    Input: nums = [3, 4, 5, 6, 1, 2]
    Output: 1
    
    Example 2:
    Input: nums = [4, 5, 0, 1, 2, 3]
    Output: 0

    """
    def findMin(self, nums: list[int]) -> int:
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2

            # If middle element is < than right pointer, the minimum resides in the left segment
            if nums[m] < nums[r]:
                r = m
             # If middle element is > than right pointer, the minimum resides in the right segment
            else:
                l = m + 1
        
        return nums[l]
    
obj1 = MinSortedArray()
print(obj1.findMin([3, 4, 5, 6, 1, 2]))
print(obj1.findMin([4, 5, 0, 1, 2, 3]))