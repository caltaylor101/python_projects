import random

words = ["hello", "goodbye"]

gameword = words[random.randint(0, len(words) - 1)]

array = []
for i in gameword:

    array.append(i)
print(array)

final = [" "] * len(gameword)
print(final)
playing = bool(1)
a=0
while playing == bool(1):
    guesses = []
    val = input("Please enter a guess: ")
    for i in guesses:
        if val == guesses:
            print("You already guessed that")
    
    answer = []
    
    
    
    while a < len(gameword):
        
        if val == array[a]:
            answer.insert(a, val)
        
        a += 1
        print(answer)
    final.append(answer)
    print(final)
    
        

