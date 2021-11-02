while True:
    n = input()
    if n == '0':
        break

    ans = "yes"
    for i in range(0, len(n) // 2):
        if n[i] != n[len(n) - 1 - i]:
            ans = "no"
            break
    print(ans)
