import time
import random
my_words = (('questionnaire','noun','a list of questions survey'),
            ('unconscious','adjective','not conscious or without awarness'),
            ('precocious','adjective','unusually mature,especially in mental development'),
            ('liaison','noun','a person who maintains a connection between people or groups'),
            ('surveillance','noun','continuous observation of a person, place , or activity in order to gather information'),
            ('malfeasance','noun','conduct by a public official that violates the public trust or is against the law'),
            ('irascible','adjective','irritable, quick-tempered'),
            ('idiosyncrasy','noun','a tendancy, habit or mannerism that is peculiar to an individual; a quirk'),
            ('foudroyant','adjective','sudden and overwhelming or stunning'),
            ('eudemonic','adjective','pertaining to conducive to happiness'))
records=()

def shuffler(word):
  list_1=list(word)
  random.shuffle(list_1)
  word=''.join(list_1)
  return word

print(('GUESS A WORD GAME').center(140,'-'))
print('\nWelcome to guess a word game!'.center(140,' '))
print('\nwhat do you want your name to be called throughout the game?')

name=str(input('please call me- '))

print(f'\nhello {name}! before jumping into the game please read the guidelines given bellow!')
print('''\n1] read the question carefully and enter your answer in the box given\n2] if you want to stop the game midway please enter "s" in the box.\n3] for each correct answer you will score one point.\n4] there are total 10 questions in the game.''')
print('\nlets start the game!')

counts=0

start_time=time.time()

for i in range(len(my_words)): 
  print(f'\nJumbled Letters: {shuffler(my_words[i][0]).upper()}')
  print(f'Part of speech: {(my_words[i][1]).upper()}')     
  print(f'Meaning: {(my_words[i][2]).upper()}')

  user_input=str(input('\nGuess the word: '))
  user_input.lower()
  
  if user_input=='s':
    break
  elif user_input == my_words[i][0]:
    print('hurray..Thats CORRECT!')
    counts+=1
  else:
    print('oh no thats WRONG!')
    print(f'the correct word is-{my_words[i][0]}')

end_time=time.time()
time_diff=(end_time-start_time)
id_1={'Guess Count','Name','Time Taken'}      
#id_2=['4','ava','60']
id_2=[counts,name,round(time_diff,2)]

records=list(records)
records.append(dict(zip(id_1,id_2)))
records=tuple(records)

if time_diff<60:
  print(f'\nYou took {time_diff//1} seconds to guess {counts} words correctly')
else:
  print(f'\nYou took {time_diff//60} minute(s) and {time_diff%60:.2f} seconds to guess {counts} words correctly')

print('\nComplete Word List')
print("-"*200)
print('##|'.rjust(3)+'Words|'.rjust(15)+'Parts of Speech|'.rjust(20)+'Meaning')

for i in range(len(my_words)):
    print('-'*200)
    print(f'{i+1:02}|'+f'{my_words[i][0]}|'.capitalize().rjust(15)+f'{my_words[i][1]}|'.capitalize().rjust(20)+f'{my_words[i][2]}'.capitalize())
print('-'*150)
print('\nLEADERBOARD')
print('-'*60)

for i in range(len(records)):
    print(f"Name:{records[i]['Name']}")
    print(f"Time Taken:{records[i]['Time Taken']}")
    print(f"Guess Count:{records[i]['Guess Count']}\n")
