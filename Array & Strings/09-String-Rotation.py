
'''
Assumeyou have a method isSubstringwhich checks if oneword is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 
'''

def isSubstr(s1: str, s2: str) -> bool:
    return s1 in s2

def isRotation(s1: str, s2: str):
    if (len(s1) == len(s2) and  len(s1) > 0):
        s1s1 = s1 + s1
        return isSubstr(s1s1, s2)
    return False;

print(isRotation("waterbottle","erbottlewat"))
