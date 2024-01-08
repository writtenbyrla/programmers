T = int(input())

for _ in range(T):
    pwd = []
    cursor = []
    word = input()

    for i in word:
        if i == '-':
            if pwd:
                pwd.pop()
        elif i == '<':
            if pwd:
                cursor.append(pwd.pop())
        elif i == '>':
            if cursor:
                pwd.append(cursor.pop())
        else:
            pwd.append(i)
    pwd.extend(reversed(cursor))
    print(''.join(pwd))