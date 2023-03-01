"""

Solution to https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

Given an array of positive integers arr, return the sum of all possible
odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.

"""

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)

        # the maximum length of the subarray
        n = length
        if length % 2 == 0:
            n -= 1
        
        subarr_len = 0
        subarr_i = 0
        output = 0
        while subarr_len <= n:
            for i in range(length):
                subarr = arr[i:i + subarr_len + 1]
                # only add subarray to the sum if it is an odd # of elements
                # and keep track to only add longer subarrays after increasing
                # length (to not repeat sums)
                if len(subarr) % 2 != 0 and len(subarr) > subarr_i:
                    sum_subarr = sum(subarr)
                    output += sum_subarr
            subarr_len += 2
            subarr_i += 2
        return output
    
if __name__ == '__main__':
    arr = [1,4,2,5,3]
    A = Solution()
    print(A.sumOddLengthSubarrays(arr))
