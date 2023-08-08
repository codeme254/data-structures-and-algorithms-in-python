def naive_string_count(long, short):
    count = 0
    for i in range(0, len(long)):
        for j in range(0, len(short)):
            if i + j >= len(long):
                return count
            if short[j] != long[i + j]:
                break
            if j == len(short) - 1:
                count += 1
    return count

print(naive_string_count("wow, you came, just wow", "wow"))
