from letter_position import LetterState

class Wordle:
    
    max_attempt = 6
    word_length = 5

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        pass 

    def attempt(self, word : str):
        word = word.upper()
        self.attempts.append(word)

    def guess(self, word: str):
        word = word.upper()
        result = []

        for i in range(self.word_length):
            character = word[i]
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character == self.secret[i]
            result.append(letter)

        return result

    @property
    def solved_game(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.max_attempt - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.solved_game
    
