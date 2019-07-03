import random

words = ["hello", "from", "the", "other", "side"]

#retrieves random word to play with
gameword = words[random.randint(0, len(words) - 1)]


playing = bool(1)



failLimit = int(len(gameword) / 2)
print(gameword)
guess = [" "] * len(gameword)

while playing == bool(1):
    #Sets count to identify each character in gameword
    a = 0
    
    val = input("Please enter a guess: ")
    
    
    
    
    
    while a < len(gameword):
        print(a)
        if val == gameword[a]:
            guess[a] = gameword[a]
  
        a += 1
        
    print(guess)

    if guess == gameword:
        print("Congratulations the word was, " + gameword)
        playing = bool(0)
    
    #Win condition question

    if failLimit == 0:
        finalguess = input("Please make your final guess: ")
        if finalguess == gameword:
            print("Congratulations, you win!")
        else:
            print("Sorry, you lose!")
        break
            
    win = input("Would you like to guess the answer (y/n)?")
    if win == "y":
        answer = input("What is the word?")
        if answer == gameword:
            print("Congratulations, you win!!!")
            playing = bool(0)
        else:
            print("I'm sorry that is not the word. You lose.")
            print(gameword)
            print(answer)
            playing = bool(0)
    else:
        print("continue on!")
        print("You have " + str(failLimit) + " more guesses.")
        
    if failLimit == 0:
        print("You failed too many time. You lose.")
        playing = bool(0)
    failLimit = failLimit - 1
    
    
        

