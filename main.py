import random
import sys

def compare_nums(guess, num):
    guess_str = str(guess)
    num_str = str(num)
    matching_list = ['X', 'X', 'X', 'X']
   # matching_str = "XXXX"
    for char in num_str:
        if char in guess_str:
            if num_str.index(char) == guess_str.index(char):
                matching_list[num_str.index(char)] = char
    revealed = "".join(matching_list)
    return revealed

def main():

    print("Welcome to Mastermind!")
    print("Can you guess the four-digit number?")

    print("Choosing number . . .")

    num =random.randint(1000, 9999)
    print(num)

    running = True

    while running == True:



        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Not a valid input. Exiting program...")
            sys.exit()


        if guess <= 999 or guess >= 10000:
            print("Invalid guess. Must be a positive four-digit number.")
        elif guess == num:
            print(f"You are the Mastermind! The number was {num}")
            print("Play again sometime!")
            running = False

            # play_again = input("Play again? Y/N ")
            # if play_again == "Y":
            #     running = False
            #     main()
            # elif play_again == "N":
            #     print("Thanks for playing!")
            #     running = False

        else:
            revealed = compare_nums(guess, num)
            print(f"Correctly guessed digits: {revealed}. Guess again!")
            continue

if __name__ == '__main__':
    main()
