import random

#1დან 100მდე პროგრამა შემთხვევითობის პრინციპით აგენერირებს რიცხვს, რომელიც უნდა გამოიცნოს მომხმარებელმა 6 ცდაში
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 6

    print("Welcome to Guess the Number!")
    print("I picked a number from 1 to 100. You have 6 attempts to guess it.")
    #ციკლი, სანამ მცდელობების რაოდენობა 0ზე მეტია მუშაობს შემდეგი პროგრამა:
    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            return
        #ასევე იპრინტება დარჩენილი მცდელობების რაოდენობა
        attempts -= 1
        print(f"Attempts left: {attempts}")
    #თუ ვერ გამოვიცანით, შესაბამისი ტექსტი იბეჭდება:
    print(f"Sorry, you ran out of attempts. The number was {number_to_guess}.")

guess_the_number()
