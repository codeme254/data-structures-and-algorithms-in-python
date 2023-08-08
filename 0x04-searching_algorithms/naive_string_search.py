def count_string_appearance(parent_string, string):
    if len(string) > len(parent_string):
        return 0
    if len(string) == len(parent_string) and string != parent_string:
        return 0
    if len(string) == len(parent_string) and string == parent_string:
        return 1
    count = 0
    i = 0
    while i < len(parent_string):
        j = 0
        for j in range(0, len(string)):
            matching = True
            if i >= len(parent_string):
                return count
            if string[j] == parent_string[i]:
                i += 1
                continue
            elif string[j] != parent_string[i]:
                i += 1
                matching = False
                break
        if matching:
            count += 1
    return count

print(count_string_appearance("wow, you are here, just wow, wow, wow", "wow"))
print(count_string_appearance("wow, you are here, just wow, wow, wow", "w"))
print(count_string_appearance("wowmzgwow", "wow"))