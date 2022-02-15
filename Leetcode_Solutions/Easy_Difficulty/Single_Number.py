#15/02/2022

#Time Complexity: O(n)
#Space Complexity: O(1) (constant)
#Faster than 66% of all solutions


def singleNumber(nums):
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i-1]:
                return nums[i - 1]
                break

        return nums[-1]


#example 
number_list = [1, 3, 4, 2, 8, 9, 7, 6, 1, 5, 2, 3, 4, 6, 7, 9, 8]

lonely_num = singleNumber(number_list)

print(f'from list {number_list}, \n number without a pair is {lonely_num}')
