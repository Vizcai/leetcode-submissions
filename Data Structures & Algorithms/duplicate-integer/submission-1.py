class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        base : dict[int[int]] = {}
        list_notduplicates :list[int] = list(set(nums))
        for num in list_notduplicates:
            base[num] = 0
        for num in nums:
            base[num] += 1
        for key in base.keys():
            if base[key] > 1:
                return True
        return False
