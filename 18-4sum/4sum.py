class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res, quad = [], []

        def kSum(k, start, current_target):
            # Base Case: When k reduces to 2, use standard Two Pointers
            if k == 2:
                left, right = start, len(nums) - 1
                while left < right:
                    two_sum = nums[left] + nums[right]
                    
                    if two_sum < current_target:
                        left += 1
                    elif two_sum > current_target:
                        right -= 1
                    else:
                        res.append(quad + [nums[left], nums[right]])
                        left += 1
                        # Skip duplicates to avoid duplicate quadruplets
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                return

            # Recursive Case: Loop through and reduce k by 1
            for i in range(start, len(nums) - k + 1):
                # Skip duplicate elements for the current slot
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Early termination optimizations (optional but makes it faster)
                # If the smallest possible k elements exceed target, stop looking
                if nums[i] * k > current_target:
                    break
                # If the largest possible k elements are less than target, skip this i
                if nums[i] + nums[-1] * (k - 1) < current_target:
                    continue

                quad.append(nums[i])
                kSum(k - 1, i + 1, current_target - nums[i])
                quad.pop()

        # Start the recursion for 4 elements starting at index 0
        kSum(4, 0, target)
        return res