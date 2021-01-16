'''
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
'''
#Method: Using While and Compare
#Time:O(N)
#Space:O(N)

def oneAway(str1, str2):
    if abs(len(str1)-len(str2)) > 1:
        return False
    
    if len(str1) < len(str2):
        s_short = str1
        s_long = str2
    else:
        s_short = str2
        s_long = str1
        
    idx1 = 0;
    idx2 = 0;
    diff = False;
    
    while idx1 < len(s_short) and idx2 < len(s_long):
        if s_short[idx1] != s_long[idx2]:
            if diff:
                return False
            diff = True
            if len(s_short) == len(s_long):
                idx1 += 1
        else:
            idx1 += 1
        idx2 += 1
    
    return True


print(oneAway('pale', 'bale'))
print(oneAway('pale', 'bake'))