N = int(input())
data = [input() for _ in range(N)]
chars = set()
char_count = {}
char_to_num = {}

for word in data:
    for i in range(len(word)):
        chars.add(word[i])
        char_count[word[i]] = char_count.get(word[i], 0) + 10**(len(word) - i - 1)

chars = sorted(list(chars), key=lambda x: char_count[x], reverse=True)
num = 9
for char in chars:
    char_to_num[char] = num
    num -= 1

total = 0

for char in char_count.keys():
    total += char_count[char] * char_to_num[char]

print(total)
