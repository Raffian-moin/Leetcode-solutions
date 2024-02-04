s = input()
currentWord = ""
result = ""

for i in range(len(s)):
    if s[i] == " ":
        if len(result) and len(currentWord):
            currentWord = currentWord + " "

        result = currentWord + result
        currentWord = ""
    else:
        currentWord += s[i]

if len(result) and len(currentWord):
    currentWord = currentWord + " "

result = currentWord + result

print(result)