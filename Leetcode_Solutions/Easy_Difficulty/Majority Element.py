
#the leetcode problem said that the majority element was the one which appeared at least half of the time
#you can sort the array and the item in the middle will be guaranteed to be the most common element


def majorityElement(nums]):     
  
  nums.sort()
    
  return nums[len(nums)//2]
        
