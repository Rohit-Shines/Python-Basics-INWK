def twosum(nums, target):
    hashTable = {}   # Creates and empty
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums:
            print("The output ", target, "is the sum of indices: (", nums[i], ",", complement, ")")
        hashTable[nums[i]] = nums[i]


twosum([2, 7, 11, 15], 9)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        ""