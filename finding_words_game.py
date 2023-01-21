import random

num_letters = 6 
num_words = 10

# accessing the word repository 
words = []
with open("100k_word_repository.txt") as word_repo:
    words = word_repo.read().split()

# getting a list of letters to choose from
alphabet = [letter for letter in "qwertyuiopasdfghjklzxcvbnm"]
vowel_count = 0
while vowel_count < 2 or vowel_count > 3:
    letters = []
    vowel_count = 0
    for x in range(0,num_letters):
        letters.append(alphabet[random.randint(0,25)])
    for letter in letters:
        if letter in [i for i in "aeiouy"]:
            vowel_count +=1
    

# getting a list of words from the letters
chosen_words = []
for word in words:
    success = True
    for letter in word:
        if letter not in letters:
            success = False
    
    if success and len(word) > 1:    
        chosen_words.append(word)

print(letters)
print(chosen_words)