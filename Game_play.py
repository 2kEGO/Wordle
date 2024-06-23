from main import Wordle
from typing import List
from letter_position import LetterState
from colorama import Fore
import random

def main():
    print('Welcome to Wordle')

    word_set = load_word_set("Personal project/Wordle/Convert_word.py")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input('Enter 5 letters word:').upper()

        if len(x) != wordle.word_length:
            print(
                Fore.RED
                + f"Word must be {wordle.word_length} characters!"
                + Fore.RESET)
            continue

        wordle.attempt(x)
        display_result(wordle)
        # print(*result, sep="\n")

    if wordle.solved_game:
        print('Congratulation, You have solved the puzzle')
    else:
        print('You have failed')
        print(f"The answer was: {wordle.secret}")

def display_result(wordle: Wordle):
    print('\n')
    print(f'You have {wordle.remaining_attempts} attempts remaining\n')
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)
    
    for _ in range(wordle.remaining_attempts):
        print(' '.join(['_'] * wordle.word_length))

def load_word_set(path: str):
    word_set = set()
    with open(path, 'r') as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
        return word_set

def convert_result_to_color(result: list[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.RED
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return ' '.join(result_with_color)

def draw_boder(line: list[str], size: int, pad: int=1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print('|' + space + line + space + '|')
    print(bottom_border)

if __name__ == '__main__':
    main()