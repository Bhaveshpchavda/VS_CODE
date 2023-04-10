# # class Book:
# #     def __init__(self, title, author):
# #         self.title = title
# #         self.author = author

# #     def get_description(self):
# #         pass

# # class EBook(Book):
# #     def __init__(self, title, author, format, num_pages):
# #         super().__init__(title, author)
# #         self.format = format
# #         self.num_pages = num_pages

# #     def get_description(self):
# #         return f"{self.title} by {self.author} ({self.format}, {self.num_pages} pages)"

# # class AudioBook(Book):
# #     def __init__(self, title, author, format, track_length):
# #         super().__init__(title, author)
# #         self.format = format
# #         self.track_length = track_length

# #     def get_description(self):
# #         return f"{self.title} by {self.author} ({self.format}, {self.track_length} minutes)"

# # class Library:
# #     def __init__(self):
# #         self.books = []

# #     def add_book(self, book):
# #         self.books.append(book)
# #         print(f"{book.title} by {book.author} added to the library.")

# #     def remove_book(self, book):
# #         self.books.remove(book)
# #         print(f"{book.title} by {book.author} removed from the library.")

# #     def search_books(self, search_term):
# #         for book in self.books:
# #             if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower():
# #                 print(book.get_description())

# # library = Library()

# # while True:
# #     print("\nLibrary Menu:")
# #     print("1. Add an audio book")
# #     print("2. Add an ebook")
# #     print("3. Remove a book")
# #     print("4. Search for books")
# #     print("5. Exit")

# #     choice = input("Enter a number: ")

# #     if choice == '1':
# #         title = input("Enter the book title: ")
# #         author = input("Enter the book author: ")
# #         format = input("Enter the format (MP3, WMA, WAV): ")
# #         if format not in ["MP3", "WMA", "WAV"]:
# #             print("Invalid format")
# #             continue
# #         track_length = input("Enter the track length in minutes: ")
# #         try:
# #             track_length = int(track_length)
# #         except ValueError:
# #             print("Invalid track length")
# #             continue
# #         book = AudioBook(title, author, format, track_length)
# #         library.add_book(book)
# #     elif choice == '2':
# #         title = input("Enter the book title: ")
# #         author = input("Enter the book author: ")
# #         format = input("Enter the format (PDF, EPUB, MOBI, AZW): ")
# #         if format not in ["PDF", "EPUB", "MOBI", "AZW"]:
# #             print("Invalid format")
# #             continue
# #         num_pages = input("Enter the number of pages: ")
# #         try:
# #             num_pages = int(num_pages)
# #         except ValueError:
# #             print("Invalid number of pages")
# #             continue
# #         book = EBook(title, author, format, num_pages)
# #         library.add_book(book)
# #     elif choice == '3':
# #         title = input("Enter the book title: ")
# #         author = input("Enter the book author: ")
# #         for book in library.books:
# #             if book.title == title and book.author == author:
# #                 library.remove_book(book)
# #                 break
# #         else:
# #             print(f"{title} by {author} not found in the library.")
# #     elif choice == '4':
# #         search_term = input("Enter the search term: ")
# #         library.search_books(search_term)
# #     elif choice == '5':
# #         print("Goodbye!")
# #         break
# #     else:
# #         print("Invalid choice")

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def get_description(self):
#         return f"{self.title} by {self.author}"

# class EBook(Book):
#     valid_formats = ["PDF", "EPUB", "MOBI", "AZW"]
    
#     def __init__(self, title, author, format, num_pages):
#         super().__init__(title, author)
#         self.format = format
#         self.num_pages = num_pages
        
#     def get_description(self):
#         return f"{super().get_description()} - EBook ({self.format}, {self.num_pages} pages)"

# class AudioBook(Book):
#     valid_formats = ["MP3", "WMA", "WAV"]
    
#     def __init__(self, title, author, format, track_length):
#         super().__init__(title, author)
#         self.format = format
#         self.track_length = track_length
        
#     def get_description(self):
#         return f"{super().get_description()} - AudioBook ({self.format}, {self.track_length} minutes)"

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def remove_book(self, title, author):
#         for book in self.books:
#             if book.title == title and book.author == author:
#                 self.books.remove(book)
#                 return True
#         return False

#     def search(self, term):
#         results = []
#         for book in self.books:
#             if term.lower() in book.title.lower() or term.lower() in book.author.lower():
#                 results.append(book)
#         return results
    
#     def get_books(self):
#         return self.books

# library = Library()

# while True:
#     print("\nMenu:")
#     print("1. Add book")
#     print("2. Remove book")
#     print("3. Search for book")
#     print("4. Show all books")
#     print("5. Quit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         book_type = input("Enter book type (EBook or AudioBook): ")
#         title = input("Enter title: ")
#         author = input("Enter author: ")

#         if book_type == "EBook":
#             format = input("Enter format (PDF, EPUB, MOBI, or AZW): ")
#             num_pages = int(input("Enter number of pages: "))
#             book = EBook(title, author, format, num_pages)
#         elif book_type == "AudioBook":
#             format = input("Enter format (MP3, WMA, or WAV): ")
#             track_length = int(input("Enter track length in minutes: "))
#             book = AudioBook(title, author, format, track_length)
#         else:
#             print("Invalid book type.")
#             continue

#         library.add_book(book)
#         print(f"Added {book.get_description()} to the library.")

#     elif choice == 2:
#         title = input("Enter title: ")
#         author = input("Enter author: ")

#         if library.remove_book(title, author):
#             print(f"Removed {title} by {author} from the library.")
#         else:
#             print(f"{title} by {author} was not found in the library.")

#     elif choice == 3:
#         term = input("Enter search term: ")
#         results = library.search(term)

#         if results:
#             print(f"Search results for '{term}':")
#             for book in results:
#                 print(book.get_description())
#         else:
#             print(f"No books found for '{term}'.")

#     elif choice == 4:
#         books = library.get_books()
#         if books:
#             print("All books in the library:")
#             for book in books:
#                 print(book.get_description())
#         else:
#             print("The library is empty.")

#     elif choice == 5:
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice. Please try again.")


class Book:
    def __init__(self, book, author):
        self.title = book.split('.')[0]
        self.b_format = book.split('.')[1]
        self.author = author
        self.type = ""

class EBook(Book):
    def __init__(self, book, author, pages):
        super().__init__(book, author)
        self.pages = pages
        self.type = "EBook"
        if self.b_format not in ['pdf', 'epub', 'mobi', 'azw']:
            raise Exception("Invalid format!")

    def show_details(self):
        print(f"\nBook Name: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Book Type: {self.type}")
        print(f"Book Format: {self.b_format}")
        print(f"Book Length: {self.pages}pgs")

class AudioBook(Book):
    def __init__(self, book, author, length):
        super().__init__(book, author)
        self.length = length
        self.type = "AudioBook"
        if self.b_format not in ['mp3', 'wma', 'wav']:
            raise Exception("Invalid format!")

    def show_details(self):
        print(f"\nBook Name: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Book Type: {self.type}")
        print(f"Book Format: {self.b_format}")
        print(f"Book Length: {self.length}")

book1 = EBook('Book1.pdf', 'author1', '250')
book2 = AudioBook('Book2.wav', 'author2', '2:2:25')
# book2 = EBook('Book3.pptx', 'author3', '300') #ERROR
book1.show_details()
book2.show_details()
