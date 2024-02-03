''' Ця функція повинна приймати суму, яку потрібно 
видати покупцеві, і повертати словник із кількістю 
монет кожного номіналу, що використовуються для формування 
цієї суми. Наприклад, для суми 113 це буде словник 
{50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним, 
тобто спочатку вибирати найбільш доступні номінали монет.'''

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum: int) -> dict:
    sum_of_coins = dict()
    for coin in coins:
        count = sum // coin
        if count > 0:
            sum_of_coins[coin] = count
        sum = sum - coin * count
    return sum_of_coins

if __name__ == "__main__":
    print(find_coins_greedy(113))