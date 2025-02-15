str=input()
contains_digit = False
for char in str:
    if char.isdigit():
        contains_digit=True
        break


if contains_digit:
    print("Yes, it contains a digit.")
else:
    print("No, it does not contain.")