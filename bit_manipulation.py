class NumberOfOneBits:
    """
    ou are provided with an unsigned integer n. Your task is to determine the number of 1 bits present in its binary representation.
    You can assume that n is a non-negative integer that fits within 32 bits.

    Example 1:
    Input: n = 5
    Output: 2
    Explanation: Binary representation of 5: 101
    
    Example 2:
    Input: n = 2147483647
    Output: 31
    Explanation: Binary representation of 2147483647: 1111111111111111111111111111111
    """
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # Clear the least significant 1 bit and add the hamming weight to res
            n = n & n-1
            res += 1

        return res

# obj1 = NumberOfOneBits()
# print(obj1.hammingWeight(5))
# print(obj1.hammingWeight(2147483647))

class CountingBits:
    """
    Given an integer n, count the number of 1 bits in the binary representation of every number in the range [0, n].
    Return an array output where output[i] is the number of 1 bits in the binary representation of i.
    Example 1:
    Input: n = 3
    Output: [0,1,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    """
    def countBits(self, n: int) -> list[int]:
        count = [] * (n + 1)
        for num in range(n+1):
            pass

            
print(7 & 1)
# obj2 = CountingBits()
# obj2.countBits(3)