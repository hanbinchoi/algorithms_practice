n = int(input("잔돈 입력:"))
count = 0

coins = [500,100,50,10]

for coin in coins:
    # / -> 연산 결과 float, // -> 연산 결과 int
    count += n//coin
    n %= coin

print(count)