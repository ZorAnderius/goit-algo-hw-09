'''
Ця функція також повинна приймати суму для видачі решти, 
але використовувати метод динамічного програмування, щоб 
знайти мінімальну кількість монет, необхідних для формування 
цієї суми. Функція повинна повертати словник із номіналами 
монет та їх кількістю для досягнення заданої суми найефективнішим 
способом. Наприклад, для суми 113 це буде словник 
{1: 1, 2: 1, 10: 1, 50: 2}
'''

coins = [50, 25, 10, 5, 2, 1]

def find_min_coins(sum:int) -> dict:
    min_coins = [0] + [float('inf')] * sum
    last_coin = [0] * (sum + 1)
    
    for value in range(1, sum + 1):
        for coin in coins:
            if value >= coin and min_coins[value] > min_coins[value - coin] + 1:
                min_coins[value] = min_coins[value - coin] + 1
                last_coin[value] = coin
    
    sum_of_coins = dict()
    current_sum = sum
    while current_sum > 0:
        coin = last_coin[current_sum]
        sum_of_coins[coin] = sum_of_coins.get(coin, 0) + 1
        current_sum -= coin
        
    return sum_of_coins

if __name__ == "__main__":
    print(find_min_coins(113))