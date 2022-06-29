# S4 문서 검색

doc = input()
word = input()
i = 0
result = 0

while i <= len(doc) - len(word):
    if doc[i:i + len(word)] == word:
        result += 1
        i += len(word)
    else:
        i += 1

print(result)