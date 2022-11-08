import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
  word = random.choice(words)
  while '-' in word or ' ' in word:
      word = random.choice(words)
  
  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()

  lives = 7

  while len(word_letters) > 0 and lives > 0:
    print('you have',lives, 'lives and you have used these letters: ', ''.join(used_letters))

    word_list = [letter if letter in used_letters else '-' for letter in word]
    print(lives_visual_dict[lives])
    print('Current word: ', ''.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
           word_letters.remove(user_letter)
           print('')

        else: 
          lives = lives - 1 
          print('\n Your letter',user_letter,'is not in the word, try again')
      
    elif user_letter in used_letters:
        print('you have already guessed',user_letter,'guess again')

    else:
        print('invalid input, try another letter')

  if lives == 0:
    print(lives_visual_dict[lives])
    print("HANGMAN: GAME OVER!")
    print('The word was: ',word)
  else:
    print('You guessed correctly! Your word is',word)
  
if __name__ == '__main__': 
  hangman()

