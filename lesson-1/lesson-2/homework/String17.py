my_string = input()
vowels = "aeiouAEIOU"
new_string = ""

for char in my_string:
    if char in vowels:
        new_string += "*"
    else:
        new_string += char

print(f"{new_string}")




