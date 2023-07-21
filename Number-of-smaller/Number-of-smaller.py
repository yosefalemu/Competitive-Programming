n, m = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_m = list(map(int, input().split()))

i, j = 0, 0
last_printed = 0

while i < n and j < m:
    while i < n and arr_n[i] < arr_m[j]:
        i += 1
    else:
        i -= 1

    print(i + 1, end=" ")
    j += 1
    i += 1

while j < m:
    print(i, end=" ")
    j += 1
