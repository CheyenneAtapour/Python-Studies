class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run = [nums[0]]
        for i in range(1, len(nums)):
            run.append(run[i-1] + nums[i])
        return run