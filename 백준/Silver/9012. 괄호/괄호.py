T = int(input())
pair = {')': '('}

for i in range(T):
    stack = []
    s = input()
    isVPS = True

    for char in s:
        if char not in pair:
            stack.append(char)
        else:
            if stack:
                stack.pop()
            elif not stack:
                isVPS = False
                break

    if not stack and isVPS:
        print('YES')
    else:
        print('NO')		