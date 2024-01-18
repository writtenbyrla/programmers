import string
import sys

input_word = sys.stdin.readline().strip()
result = [-1] * len(string.ascii_lowercase)

for i in range(len(input_word)):
    char = input_word[i]
    idx = ord(char) - ord('a')
    if result[idx] == -1:
        result[idx] = i

print(*result)