txt = str(input())

result = ""
count = 0

for i in range(len(txt)):
    if (count + 1) % 3 == 0 and txt[i] not in "aeiouAEIOU" and txt[i] != "_":
        result += "_"

    result += txt[i]
    count += 1

print(result)
