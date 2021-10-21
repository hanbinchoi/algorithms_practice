n = int(input())
distance = [int(i) for i in input().split()][:n-1]
price = [int(i) for i in input().split()][:n]

total = 0
n_price = 10001
for i in range(len(price)-1):
    if n_price > price[i]:
        n_price = price[i]
    print(n_price,price[i])
    total += distance[i] * n_price

print(total)