from exceptions import WordleException
from pathlib import Path
import re

class Wordle:
    def __init__(self, word: str):
        """
        wordle word of length 5
        """
        dictionary = open(Path(__file__).parent.parent.joinpath('files/words.txt'), "r")
        allowed_words = dictionary.readlines()
        dictionary.close()
        allowed_words = [x.upper().strip() for x in allowed_words]
        word = word.upper()
        if len(word) != 5:
            raise WordleException(
                f'The length of the word must be exactly 5.'
            )
        if not word.isalpha():
            raise WordleException(
                f'The word must only contain English alphabets.'
            )
        if word not in allowed_words:
            raise WordleException(
                f'The word is not allowed. Choose a different word.'
            )
        self.word = word
    
    def displayWord(self):
        """
        display the word
        """
        print(f'The word is: {self.word}')

    def getMatch(self, attempt: str) -> list[bool]:
        """
        get the match of an attempt as a list of int.
        if position of the match is correct, match at position is 2
        if the character is in the correct word but in the wrong position, match at position is 1
        if the character is not in the correct word, match at position is 0
        """
        attempt = attempt.upper()
        match = []
        for i in range(5):
            if attempt[i] == self.word[i]:
                match.append(2)
            elif attempt[i] in self.word:
                match.append(1)
            else:
                match.append(0)
        return match

    
    def solveWordle(self):
        """
        solve for the correct word
        """
        # load list of possible words
        dictionary = open(Path(__file__).parent.parent.joinpath('files/words.txt'), "r")
        allowed_words = dictionary.readlines()
        dictionary.close()
        possible_words = [x.upper().rstrip('\n') for x in allowed_words]
        # initialize search
        turn_count = 1
        attempt_word = "REACT"
        while sum(self.getMatch(attempt_word)) < 10 and turn_count < 7:
            match = self.getMatch(attempt_word)



if __name__ == '__main__':
    wordle = Wordle('serve')
    match = wordle.getMatch('trash')
    print(match)