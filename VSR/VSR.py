import sys

t = int(input())

while t > 0:
    a, b = map(int,sys.stdin.readline().split())
    print(2 * a * b / (a + b))
    t = t - 1
