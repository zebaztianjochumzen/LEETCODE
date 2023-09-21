"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""
import math

"""Funktionen for index,x in enumerate(nums) går igenom listan och returna listans index samt listans element, 
    Därefter så gör vi samma sak fast för tal två (y) och sedan så kollar vi om elementen summeras till det som skickas in. 
    Vi kollar även så att elementen inte kan vara dubletter eftersom att index måste var skilt från position. 

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         for index,x in enumerate(nums):
            for position,y in enumerate(nums):
                if x + y == target and index != position:
                    return [index,position]