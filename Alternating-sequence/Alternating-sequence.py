t = int(input())

def sign(n):
    return n > 0

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    i = 0
    while i < n:
        max_val = arr[i]
        j = i
        while j < n and (sign(arr[i]) == sign(arr[j])):
            max_val = max(max_val, arr[j])
            j += 1
        ans += max_val
        i = j
    print(ans)
