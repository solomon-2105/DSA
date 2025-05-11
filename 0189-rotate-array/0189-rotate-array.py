class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # To handle cases when k > n

        # Helper function to reverse a part of the array in-place
        def reverse_section(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse_section(0, n - 1)

        # Step 2: Reverse the first k elements
        reverse_section(0, k - 1)

        # Step 3: Reverse the remaining elements from k to n-1
        reverse_section(k, n - 1)
