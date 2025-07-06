import random
import sys

def compare_nums(guess, num):

    guess_list = list(map(int, str(guess)))
    num_list = list(map(int, str(num)))
    matching_list = ['X', 'X', 'X', 'X']

    for i in range(0,4):
        if guess_list[i] == num_list[i]:
            matching_list[i] = str(guess_list[i])
    revealed = "".join(matching_list)
    return revealed
        

def main():

    print("**********************")
    print("Welcome to Mastermind!")
    print("Can you guess the four-digit number?")

    print("Choosing number . . .")

    running = True

    num =random.randint(1000, 9999)
   

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

            while True:
                play_again = input("Play again? y/n ")
                if play_again.lower() == "y":
                    main()
                elif play_again.lower() == "n":
                    running = False
                    break
                else:
                    print("Invalid input")
                    continue

        else:
            revealed = compare_nums(guess, num)
            print(f"Correctly guessed digits: {revealed}. Guess again!")
            continue

if __name__ == '__main__':
    while True:
        restart = main()
        if not restart:
            print("Thank you for playing!")
            print("**********************")
            break
