class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        even = [-1] * len(nums) 
        odd = [-1] * len(nums)

      
        
        def dfs_odd(i):
            if i >= len(nums):
                return 0
            if odd[i] != -1:
                return odd[i]

            odd[i] = max(dfs_odd(i + 1) , nums[i] + dfs_odd(i + 2))
            
            return odd[i]

        def dfs_even(i):
            if i >= (len(nums) -1):
                return 0
            if even[i] != -1:
                return even[i]

            even[i] = max(dfs_even(i + 1) , nums[i] + dfs_even(i + 2))
            
            return even[i]

        even = dfs_even(0)
        odd = dfs_odd(1)

        return max(even, odd)
             