'''
return true if the string doesn't have duplicate characters
return false if the string has duplicate character by myself. 
'''
def isUnique(string):
    characters = {}
    for character in string:
        if character in characters:
            return False
        characters[character]=True
    return True

print(isUnique('asdddwef'))
print(isUnique('asdfght'))

