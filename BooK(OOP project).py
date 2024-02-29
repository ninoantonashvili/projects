#თავიდან ვქნი წიგნის კლასს შესაბამისი ატრიბუტებით
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class BookManager:
    def __init__(self):
        self.books = []
#წიგნის დამატების მეთოდი, რომელიც იღებს სახელს, ავტორს და წელს
    def add_book(self, title, author, year):
        def add_book(self, title, author, year):
            # აქ მოწმდება შეიყვანა თუ არა მომხმარებელმა ატრიბუტების მნიშვნელობები

            if not all([title, author, year]):
                print("Invalid input. Please provide title, author, and year.")
                return

            try:
                year = int(year)
                if year < 1800 or year > 2024:
                    raise ValueError("Year must be between 1800 and 2024.")
            except ValueError as e:
                print(f"Invalid year: {e}")
                return
            # ამის შემდეგ იქმნება წიგნის ახალი ობიექტი, რომელიც შეიცავს მომხმარებლის მიერ მიწოდებულ ინფორმაციას
            book = Book(title, author, year)
            self.books.append(book)
            print("Book added successfully.")


        #ახლა ვქმნი მეთოდს, რომელიც აჩვენებს წიგნების სიას, რომელიც უკვე დამატებულია ჩვენს "ბიბლიოთეკაში"
    def show_all_books(self):
        print("List of all books:")
        #ციკლით გადავუყვები ყველა წიგნს, რომელიც დამატებულია და გამოვიტან კონსოლშ შესაბამისი სათაურით, ავტორითა და გამოშვების წლით
        for book in self.books:
            print(f"{book.title} by {book.author} ({book.year})")

      #შემდეგი ფუნქცია მომხმარებელს აძლევს საშუალებას, იპოვოს წიგნი სათაურის შეყვანით
    def search_by_title(self, title):
        #ვქმნი ლისთს ნაპოვნი წიგნების, რადგან შეიძლება ერთსადაიმავე სათაურს რამდენიმე წიგნი შეესაბამებოდეს
        found_books = [book for book in self.books if book.title == title]
        #თუ არსებობს ასეთი "ლისთი", დავაბეჭდინებ ყველა წიგნს, რომელიც ამ ლისთში შედის
        if found_books:
            print(f"Found {len(found_books)} book(s) with the title '{title}':")
            for book in found_books:
                print(f"{book.title} by {book.author} ({book.year})")
        else:
            print(f"No books found with the title '{title}'.")

def main():
    book_manager = BookManager()
    #ეს უკვე არის უშუალოდ მომხმარებელი რასაც ხედავს და რის მიხედვითაც მუშაობს. ეძლევა არჩევანი, დაამატოს წიგნი, ნახოს წიგნების ნუსხა, მოძებნოს წიგნი ან საერთოდ შეწყვიტოს პროგრამა:

    while True:
        print("\n1. Add a new book")
        print("2. Show all books")
        print("3. Search for a book by title")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year = input("Enter the year of publication: ")
            book_manager.add_book(title, author, year)
        elif choice == "2":
            book_manager.show_all_books()
        elif choice == "3":
            title = input("Enter the title of the book to search for: ")
            book_manager.search_by_title(title)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
