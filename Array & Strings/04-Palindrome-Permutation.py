'''
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
'''

#Method: Using dict
#Time: O(N)
# Space: O(N) 

def isPalindromePermutation(str):
    #delete whitespaces
    str = str.replace(' ','')
    #convert to similar case
    str = str.lower()
    letters = {}

    for i in str:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    odd_counter = 0
    for k,v in letters.items():
        if v % 2 != 0 and odd_counter == 0:
            odd_counter += 1
        elif v % 2 != 0 and odd_counter != 0:
            return False
    return True

print(isPalindromePermutation('Tact Coa'))