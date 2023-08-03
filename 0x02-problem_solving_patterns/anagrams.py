# Given two strings, write a function to determine if the second string is an anagram of the first. An anagram is a word, phrase or name formed by rearranging the letters of another eg cinema is formed from iceman

def validAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1_lookup = {}
    str2_lookup = {}
    for i in range(0, len(str1)):
        current_char = str1[i]
        if not str1_lookup.get(current_char):
            str1_lookup[current_char] = 1
        else:
            str1_lookup[current_char] += 1
    
    for i in range(0, len(str2)):
        current_char = str2[i]
        if not str2_lookup.get(current_char):
            str2_lookup[current_char] = 1
        else:
            str2_lookup[current_char] += 1
    
    for key, value in str1_lookup.items():
        if not str2_lookup.get(key):
            return False
        if str2_lookup[key] != value:
            return False
        else:
            continue
    return True

print(validAnagram('aaz', 'zza'))
print(validAnagram('anagram', 'nagaram'))
print(validAnagram('rat', 'car'))
print(validAnagram('cinema', 'iceman'))
print(validAnagram('', ''))