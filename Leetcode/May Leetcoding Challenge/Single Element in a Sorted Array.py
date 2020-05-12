'''  
    540. Single Element in a Sorted Array
    https://leetcode.com/problems/flood-fill/
    12/05/2020
    May LeetCoding Challenge
    Day-12
    Level: Easy
    
    You are given a sorted array consisting of only integers where every element appears exactly twice, 
    except for one element which appears exactly once. Find this single element that appears only once.
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d = Counter(nums)
        for i in d:
            if d[i] == 1:
                return i
