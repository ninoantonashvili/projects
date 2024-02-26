#მარტივი კალკულატორის პროგრამა, ჯერ განვსაზღვრავ ფუნქციებს, რომლებიც გამოყენებული იქნება:
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

#აქ მომხმარებელი ირჩევს რომელ ოპერაცია,უნდა რომ შესრულდეს კალკულაციისას.
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):

        try:
            # შემდეგ შეგვყავს ორი რიცხვი, რომლებიც ჯერ float-ში გადამყავს
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            #თუ მომხმარებელმა არ შეიყვანა რიცხვი, ამოაგდებს ერორს
            print("enter a valid number")
            continue

        #ამის მერე, უკვე კონსოლზე იბეჭდება შესაბამისი შედეგი.
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))

        break
    else:
        print("Invalid input")
