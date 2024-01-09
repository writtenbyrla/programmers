pair = {')' : '(', ']' : '['}

while(True):
    sentence = input()

    if sentence == ".": break

    stack = []
    result = True

    for char in sentence:
        if char in '([':
            stack.append(char)

        elif char in ')]':
            if len(stack)!=0 and stack[-1] == pair[char]:
                stack.pop()
            else:
                stack.append(char)
                result = False
                break

    if not stack and result:
        print('yes')
    else:
        print('no')