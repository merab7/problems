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


here i will just add the 3sum problem brut force solution and will continue it tomorrow:

class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort() აქ ხდება დასორტვა სამიზნე ლისტისა. მიზანი კი დუბლიკატების აღმოჩენიაა და პოინტერების ლოგიკური გამოყენბაა

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: პირველრიგში ვამოწმბთ დასორტვის შემდეგ თუ პირველი პოინტერი (რომელიც არაა 0 ინდექსზე) უდირს მის შემდგომ პოინტერს ანუ გამივრიცხავთ
            პირველი პოინტერის დუბლიკაციას
                continue

            j = i+1 აქ ლოგიკურად ციკლის მიხედვით ვააფდეითებთ მეორე
            k = len(nums)-1 და მესამე პოინტერებს
            while j<k: აქ განვიხილავთ არსებულ პოინტერებს მანამ სანამ მეორე პოინტერი ნაკლებნია მესამეზე
                total = nums[i] + nums[j] + nums[k] ვახდენთ სუმის იდენტიპიკაციას არსებული პოინტერებიდან
                და იმისდა მიხედვით რა მიმართებაშია სუმი 0თან  ვააბდეითებთ პოინტერებს(მეორეს და მესამეს რადგან ეს ყველაფერი ხდება ციკლში პირველი პოინტერის ფიქსაციით შემდგომ იტერაციამდე)
                if total > 0:
                    k -= 1
                elif total < 0:
                    j+=1
                else:
                თუ სუმაცია 0ის ტოლია ვახორციელებთ სასურველ შედეგობრიუვ ლისტში შესაბამისი ელემენტების დამატებას
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    აქ ვახორციელებთ მეორე პოინტერეის დუბლიკანტის გამორიცხვას.
                    ბოლო პოინტერს დუბლიკატის გამორიცხვა არ სჭირდება რადგან ზემო აღნიშნულ კლოგიკაში თუ საჭირო გახდა ბოლო პოინტერის მარცხნიუვ გადაადგილება რადგან სუმაცია მეტია ნულზე და მის შემდგომი მარცხნივ მდგომი მისი დუბლიკანტია ისევ იგივე ლოგიკით რადგან ისევ მეტი იქნება სუმაციოა ნულზე რადგან ზემოაღნიშნულები დუბლიკატები არიან მოხდებ ამისი ისევ მარცხნივ გადანაცვლებნა"if total>0:j-=1".
                    while nums[j] == nums[j-1] and j < k:
                        j+=1

        return result

        სამი სუმის ამ ამოხსნისას ვიყენებთ პოინტერებს და არა ჰაშ მაპოს როგორც ეს ორ სუმში გამოვიყენე
        ხდება ერთი პოინტერესი ფიქსაცია ლუპის მიხედვით i ხოლო მარცხენა და უკიდურესი მარჯვენა პოინტერების დააფდეითება
 :        ხდება შეასბამისი ლოგიკის მიხედვით რომელიც ითვალისწინებს პირველრტიგში შემდგომ იტერაცას, სუმის 0თან მიმართებაში კორელაციას და ასევე დუბლიკატების გამორიცხვას.


"""
