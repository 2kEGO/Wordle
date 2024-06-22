from main import Wordle
from letter_position import LetterState
from colorama import Fore

def main():
    print('Hello Word')
    wordle = Wordle('APPLE')

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

def display_result(wordle: Wordle):
    print('\n')
    print(f'You have {wordle.remaining_attempts} attempts remaining\n')
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)
    
    for _ in range(wordle.remaining_attempts):
        print(' '.join(['_'] * wordle.word_length))

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
    
    top_boder = ''
    
if __name__ == '__main__':
    main()