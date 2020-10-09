"""
Tower of Hanoi

See README for instructions.
"""
import os

towers = [[3, 2, 1], [], []]
total_moves = 0


def print_towers():
    """Presents a visual representation of the tower data."""
    t0 = towers[0][::]
    t0.extend([' '] * (3 - len(t0)))
    t1 = towers[1][::]
    t1.extend([' '] * (3 - len(t1)))
    t2 = towers[2][::]
    t2.extend([' '] * (3 - len(t2)))
    for a, b, c in zip(t0[::-1], t1[::-1], t2[::-1]):
        print(a, b, c)
    print('- - -')
    print('1 2 3')


def is_won():
    """Returns whether the game has been won."""
    return towers[-1] == [3, 2, 1]


def move(from_tower, to_tower):
    """Moves a disc from one tower to another."""
    global total_moves
    d = towers[from_tower - 1].pop()
    towers[to_tower - 1].append(d)
    total_moves += 1


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Total Moves: {total_moves}\n')
        print_towers()
        choice_from = int(input('\nFrom tower: '))
        choice_to = int(input('To tower: '))
        move(choice_from, choice_to)


if __name__ == '__main__':
    main()
