"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

#completed Twosday Tuesday Twosday 22.2.22
#completed Feb 22 2022



def twoSum(nums, target):
        hmap = {}
        for ind, i in enumerate(nums):
            if i in hmap.keys():
                return [hmap[i], ind]
            else:
                hmap[target - i] = ind
        
            
