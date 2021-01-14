'''
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
'''

#Method: Using RegX
#Time: O(N)
#Space: O(1)

import re
def replaceStr(str):
    return re.sub(" ","%20",str)
    
print(replaceStr('Hi I am here to learn'))






