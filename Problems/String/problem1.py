s = "aaabbbcdddddaaaaaa"
# Output - a3b3c1d5a6
out = ""
i = 0
while i < len(s):
    count = 1
    j = i + 1
    while j < len(s) and s[i] == s[j]:
        count = count + 1
        j = j + 1
    out = out + s[i] + str(count)
    i = j
print(out)
