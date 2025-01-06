"""
this is classic two sum problem.
here is two solution firts one is brutforce soluton and second is the optimal solution using hash table
here is the problem :
   Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

here is the first solution:

class Solution(object):
     def twoSum(self, nums, target):
         for index, ele in enumerate(nums) :
             if target - ele in nums and not index == nums.index(target-ele):
                 return index, nums.index(target-ele)

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


    here is the editorial form leetcode:
      https://leetcode.com/problems/two-sum/editorial

"""
