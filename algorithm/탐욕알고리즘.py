# 탐욕 알고리즘의 이해
coin_list = list(map(int,input().split(',')))

def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value//coin
        total_coin_count += coin_num
        value -= coin*coin_num
        details.append([coin, coin_num])
    return total_coin_count, details

print(min_coin_count(4720, coin_list))