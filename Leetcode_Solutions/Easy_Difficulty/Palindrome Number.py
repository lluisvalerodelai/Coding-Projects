#Feb 17 2022

#by turning the number into a string you can reverse it
#then you can check if the reversed number is == original number
#negative numbers can not be palindrome
#any number that is between 1-9 is always palindrome
#numbers that end in zero can not be palindrome

def isPalindrome(x):
         
    s_num = str(x)

    if x < 0 or x%10 == 0:
        return False
    elif s_num == 1:
        return True



    r_num = ''
    for i in reversed(s_num):
        r_num += str(i)
    if r_num == s_num:
        return True
    else:
        return False

 
isPalindrome(121)
    #True

 
isPalindrome(-34)
    #False

isPalindrome(11112222333344443333222111)
    #False
