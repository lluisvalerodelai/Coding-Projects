#Feb 17 2022

#by turning the number into a string you can reverse it
#then you can check if the reversed number is == original number
#negative numbers can not be palindrome
#any number that is between 1-9 is always palindrome
#numbers that end in zero can not be palindrome


class Solution:
    def isPalindrome(self, x: int) -> bool:
      
        if x > 0 or x%10 == 0 or len(str(x)) == 1:
          return False
      
        s_num = str(x)
        r_num = ''
        for i in reversed(s_num):
            r_num += str(i)
        if r_num == s_num:
            return True
        else:
            return False
          
          
