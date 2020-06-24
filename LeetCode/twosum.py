class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for x in range(len(nums)):
            if nums[x] in dic:
                dic[nums[x]] = [dic[nums[x]], x]
            else:
                dic[nums[x]] = x
        nums.sort()
        for i in range(len(nums)):
            if nums[i] + nums[-1] < target:
                continue
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        if (nums[i] == nums[j]):
                            return [dic[nums[i]][0], dic[nums[j]][1]]
                        return [dic[nums[i]], dic[nums[j]]]