import random

# Get user input
exp_num = int(input("Enter number of experiments: "))
num_flips = int(input("Enter number of flips per experiment: "))
streak_length = int(input("Enter streak length to check for: "))

def has_streak(coin_flips, streak_length):
    count = 1
    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            count += 1
            if count == streak_length:
                return True
        else:
            count = 1
    return False


def simulate(exp_num, num_flips, streak_length):
    streaks_found = 0
    for _ in range(exp_num):
        flips = ['H' if random.randint(0, 1) == 1 else 'T' for _ in range(num_flips)]
        if has_streak(flips, streak_length):
            streaks_found += 1
    percentage = (streaks_found / exp_num) * 100
    print(f'Chance of getting a streak of {streak_length}: {percentage:.2f}%')

simulate(exp_num, num_flips, streak_length)
