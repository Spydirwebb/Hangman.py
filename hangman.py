def print_board(wrong):
    for i in range (0,wrong):
        prop[2+i] = end[2+i]
    for i in prop:
        print (i)
    print(" ".join(score_board))

end = ["   _____",
 "  |/    |",
 "  |    (_)",
 "  |    /|\\",
 "  |     |",
 "  |    / \\",
 "  |",
 "__|______"]

prop = ["   _____",
 "  |/    |",
 "  |       ",
 "  |       ",
 "  |      ",
 "  |       ",
 "  |",
 "__|______"]
secret_word = "instant"
word = list(secret_word)
score_board = []
for char in word:
    score_board.append("_")
guesses = []
running = True
wrong = 0
while(running):
    print_board(wrong)
    print("Guesses: ")
    print(guesses)
    guess = input("Enter Guess: ")
    if guess in word:
        print("Correct")
        while guess in word:
            character_index = word.index(guess)
            score_board[character_index] = word[character_index]
            word[character_index] = "*"
    else:
        print("Incorrect")
        wrong+=1
        guesses.append(guess)
    if(wrong >=4):
        print_board(wrong)
        print ("Sorry, You Lost. The Word was: {}".format("".join(secret_word)))
        
        break
    elif("_" not in score_board):
        print_board(wrong)
        print ("You Win!")
        break
    else:
        continue

