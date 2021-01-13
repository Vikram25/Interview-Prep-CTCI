def checkPerm(str1,str2):
    if(len(str1)!=len(str2)):
        return False
    
    str1, str2 = sorted(str1), sorted(str2)
    for i in range(len(str1) - 1):
        if str1[i] != str2[i]:
            return False
    return True


print(checkPerm("asd","aew"))
print(checkPerm("dog","god"))