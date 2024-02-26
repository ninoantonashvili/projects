#project N1
import random

#თამაშის არსი შემდეში მდგომარეობს, მომხმარებელი ირჩევს pink ან black აბს, შემდეგ იღებს ან 50 დოლარს ან 1000-ს.
#ამის შემდეგ მან უნდა დახარჯოს ეს ტანხა ისე, რომ შენაძენებმა არ გადააჭარბოს არსებულ ფულს. თუ იმაზე მეტს დახარჯავს, ვიდრე აქვს,
#კარგავს ყველაფერს. იქამდე უნდა აარჩიოს ნივთები, სანამ მოგებულ თანხას არ ამოწურავს.
def main():
    print("Would you choose a PINK pill or a BLACK pill?")
    choice = input().lower()

    if choice == "pink":
        money = random.choice([50, 1000])
        if money == 50:
            print("Try your luck next time, you got only 50 dollars :(")
        else:
            print("You are lucky today! You just won 1000 dollars! Go ahead and spend it.")
    elif choice == "black":
        money = random.choice([50, 1000])
        if money == 50:
            print("Try your luck next time, you got only 50 dollars :(")
        else:
            print("You are lucky today! You just won 1000 dollars! Go ahead and spend it.")
    else:
        print("Invalid choice.")
        return

    while True:
        try:
            cost = int(input("How much does your item cost? "))
            if cost > money:
                #ზედმეტი თუ დახარჯა მომხმარებელმა, ყველაფერს კარგავს და შესაბამისი შეტყობინება გამოდის ეკრანზე:
                print("Too greedy! Now you lost everything! Go and learn some maths!")
                break
            elif cost == money:
                print("Have a nice day :)")
                break
            else:
                money -= cost
                print(f"Nice purchase! You have {money} dollars left. How much does the next item cost?")
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
