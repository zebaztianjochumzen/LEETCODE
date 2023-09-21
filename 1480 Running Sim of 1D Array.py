"""
Uppgiftsbeskrivning 
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Målet med uppgiften är alltså att vi vill ta tal nummer 1 i listan och sedan addera med tal nummer 2 i listan. 
Resultatet av det ska sedan adderas med nummer 3 i listan osv, fram till listans slut.
"""

"""
Så hur fungerar funktionen?

Funktionen fungerar som så att vi definerar att vi kollar rangen från element 1 till längden på listan, alltså det n:te talet, 
Vi tar sedan det n:te talet och subtraherar med 1 och lägger till det n:te talet?

"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range (1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums 