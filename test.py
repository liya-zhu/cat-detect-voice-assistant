def twoSum(nums, target):
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []

twoSum([4,3,1,7,6,5,9,2],9)