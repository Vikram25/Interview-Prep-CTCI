'''
 Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
'''

def stringCompression(string):
    characters = {}
    newStr = ''
    for char in string:
        if not char in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    
    for key, value in characters.items():
        newStr += key
        newStr += str(value)

    if(len(string) == len(newStr)):
        return string
    else:
        return newStr


print(stringCompression('aabbbccccddddd'))
#Above code is woring fine if input string in "aabbccdddeeefff" format but not doing well in this format('aabbbcccaaa'). 
#So lets modifiy our code 

def stringCompression1(string):
    newStr = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i-1]:
            newStr.append(string[i-1] + str(counter))
            counter  = 0
        counter += 1
    
    newStr.append(string[-1] + str(counter))
    compressed = ''.join(newStr)
    if(len(string) == len(newStr)):
        return string
    else:
        return compressed


print(stringCompression1('aabcccccaaa'))
 