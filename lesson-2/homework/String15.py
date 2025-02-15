Sentence=str(input())
a=Sentence.split()
b=''.join([word[0].upper() for word in a])
print(b)


