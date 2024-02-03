from timeit import timeit
from typing import Callable

from rich.table import Table
from rich.console import Console

from find_coins_greedy import find_coins_greedy 
from find_min_coins import find_min_coins

def draw_comparison_table(data: list, title) -> Table:
    table = Table(title=title, style="blue", show_lines=True)

    table.add_column("Algorithm", justify="center", style="green",min_width=20, no_wrap=True)
    table.add_column("Time,s (small value)", style="yellow", justify="center", max_width=35, no_wrap=False)
    table.add_column("Time,s (medium value)", justify="center",min_width=20, style="yellow")
    table.add_column("Time,s (big value)", justify="center",min_width=20, style="yellow")
    for elem in data:
        table.add_row(elem[0], f'{elem[1][0]:.5f}', f'{elem[1][1]:.5f}', f'{elem[1][2]:.5f}')
    return table

def execution_time(func: Callable, data: int):
    return timeit(lambda: func(data), number=10)

def create_row(func: Callable, arr: list, dates: list) -> list:
    times = []
    for data in dates:
        time = execution_time(func, data)
        times.append(time)
    arr.append((func.__name__, times))
    return arr

def main():
    console = Console()
    values = [113, 113038, 11308378]
    result = list()
    create_row(find_coins_greedy, result, values)
    create_row(find_min_coins, result, values)
    
    console.print(draw_comparison_table(result, 'Comparison of the execution time of the search for the optimal solution based on the greedy algorithm and the dynamic programming algorithm'))

    res_greedy = list()
    res_dynamic = list()
    for value in values:
        res_greedy.append(find_coins_greedy(value))
        res_dynamic.append(find_min_coins(value))
    diff = []
    if res_greedy and res_dynamic and len(res_greedy) == len(res_dynamic):
        for index in range(len(res_dynamic)):
            items = {key: res_dynamic[index][key] - res_greedy[index][key] for key in res_dynamic[index] if key in res_dynamic[index] and res_dynamic[index][key] == res_greedy[index][key]}
            diff.append(items)
            
    for item in diff:
        print(item)

if __name__ == "__main__":
    main()