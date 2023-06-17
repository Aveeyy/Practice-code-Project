#program : calculate the lottery
#author: Avey
#date : 4/4/2023


import random

def main():
    winning_numbers = get_winning_numbers()
    player_numbers = get_player_numbers()
    num_matches = get_matches(winning_numbers, player_numbers)
    print_numbers(winning_numbers, player_numbers, num_matches)


def get_winning_numbers():
    winning_list = []
    for i in range(6):
        winning_list.append(random.randint(1, 9))
    return winning_list

def get_player_numbers():
    player_list = []
    for _ in range(6):
        num = input("Enter a number between 1 and 9: ")
        while not num.isdigit() or int(num) < 1 or int(num) > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            num = input("Enter a number between 1 and 9: ")
        player_list.append(int(num))
    return player_list

def get_matches(winning_list, player_list):
    matches = 0
    for i in range(6):
        if player_list[i] == winning_list[i]:
            matches += 1
    return matches

def print_numbers(winning_list, player_list, matches):
    print("Winning numbers:", winning_list)
    print("Player's numbers:", player_list)
    print("Number of matches:", matches)
    if matches > 0:
        matching_numbers = [player_list[i] for i in range(6) if player_list[i] == winning_list[i]]
        print("Matching numbers:", matching_numbers)

main()


