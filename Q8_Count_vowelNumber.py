s = "education"
count = 0

for i in s:
    if i in "aeiouAEIOU":
        count += 1

print("Vowel count:", count)