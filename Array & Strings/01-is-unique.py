# Method: Using Dict
# Time: O(n)
# Space: O(n)

# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
def isUnique(string):
    characters = {}
    for character in string:
        if character in characters:
            return False
        characters[character]=True
    return True

print(isUnique('asdwefd'))
print(isUnique('asdfght'))

