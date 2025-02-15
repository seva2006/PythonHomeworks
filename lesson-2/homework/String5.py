str_input = input()
vowels = "aeiouAEIOU"
count1 = 0
count2 = 0
for char in str_input:
    if char in vowels:
        count1 += 1
    elif char.isalpha():
        count2 += 1


print("Number of vowels: " + str(count1))
print("Number of consonants: " + str(count2))


