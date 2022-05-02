def make_password(idx, pw):
    if len(pw) == L:
        count = {'consonant': 0, 'vowel': 0}
        for char in pw:
            if char in ['a', 'e', 'i', 'o', 'u']:
                count['vowel'] += 1
            else:
                count['consonant'] += 1
        if count['vowel'] >= 1 and count['consonant'] >= 2:
            answers.append(pw)
        return
    elif idx == C:
        return

    char = data[idx]
    idx += 1
    make_password(idx, pw+char)
    make_password(idx, pw)


L, C = map(int, input().split())
data = input().split()
data.sort()
answers = []
make_password(0, '')

for answer in answers:
    print(answer)