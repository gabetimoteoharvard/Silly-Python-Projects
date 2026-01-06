from colorama import Fore
import random

with open('2of12inf.txt') as words_file:
    word_list = words_file.read().strip().split('\n')
    word_list = set([x.upper() for x in word_list if len(x) == 5])

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

usage = {}
for letter in alphabet:
    usage[letter] = 0

print(Fore.BLUE + 'TERMINAL WORDLE by Gabriel Timoteo\n')
print(Fore.BLUE + 'Guess a 5 letter word')
print(Fore.BLACK + '\n')

word_to_guess = random.choice(list(word_list))
tries = 6

while tries != 0:
    for let in word_to_guess:
        usage[let] += 1

    guess = input().upper()

    print('\033[1A' + '\033[K', sep='')
    if len(guess) != 5 or guess not in word_list:
        print('Please enter a valid word\n')
        continue
        
    for x in range(5):
        if guess[x] == word_to_guess[x]:
            print(Fore.GREEN + guess[x].upper(), end='')
            print(Fore.BLACK + '', end='')
            usage[guess[x]] -= 1
            continue
        if usage[guess[x]] != 0:
            print(Fore.YELLOW + guess[x].upper(), end='')
            usage[guess[x]] -= 1
            print(Fore.BLACK + '', end='')
            continue
        print(Fore.BLACK + guess[x].upper(), end='')
    
    print('\n')
    if guess == word_to_guess:
        if tries == 6:
            print(f'You did it in 1 try!')
        else:
            print(f'You did it in {6 - tries + 1} tries')
        break
    for key in usage.keys():
        usage[key] = 0
    tries -= 1
    
           
if tries == 0:
    print(f'You were not able to guess the word\n')
    print(f'The word was {word_to_guess}')
    
    
    
