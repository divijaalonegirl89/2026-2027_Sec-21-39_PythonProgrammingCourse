#Palindrome number
num=int(input("enter a number:")) 
orig_num= num
work= num
reverse = 0
while work> 0:
    digit = work % 10
    reverse = reverse* 10 + digit
    work= work// 10
if reverse == orig_num:
   print(f"{orig_num} is a palindrome")
else:
    print(f"{orig_num} is not a palindrome")  
