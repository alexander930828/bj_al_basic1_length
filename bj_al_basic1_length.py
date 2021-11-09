import sys

input = sys.stdin.readline

word = input()

stack = []

for i in word:
    if i != ' ':
        stack.append(i)
    else:
        continue

print(len(stack)-1)