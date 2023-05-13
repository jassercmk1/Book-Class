import pandas as pd
from dataclasses import dataclass

df = pd.read_excel("Books.xlsx")
def load_df_into_dict(df) -> dict:
    df_dict = df.to_dict('records')
    return df_dict


@dataclass
class Book:
    Book_id: int
    Title: str
    Author: str
    Price: float
    Publisher: str
    ISBN: int

    @staticmethod
    def read_from_df() -> dict:
        books = {}
        df = pd.read_excel("Books.xlsx")
        df_dict = load_df_into_dict(df)
        for row in df_dict:
            book_id = row.pop('Book_id')
            row.pop('book_description', None)
            book = Book(Book_id=book_id, **row)
            books[book_id] = book
        return books

    def book_info(self) -> dict:
        return {
            "Book Id": self.Book_id,
            "Title": self.Title,
            "Author": self.Author,
            "Price": f'{self.Price:.2f}$',
            "Publisher": self.Publisher,
            "ISBN": self.ISBN}

    @staticmethod
    def books_available() -> dict:
        books = Book.read_from_df()
        if not books:
            print("No books available")
            return
        print("ALL BOOKS AVAILABLE:")
        for book in books.values():
            print(book.book_info())

    @staticmethod
    def choose_book() -> dict:
        books = Book.read_from_df()
        while True:
            print("Choose a Book !!!")
            user_input = input("Enter a Book Id: ")
            if user_input.isdigit():
                book_id = int(user_input)
                if book_id in books:
                    return books[book_id].book_info()
            print("Invalid Book Id. Please try again.")

print(Book.books_available())
print(Book.choose_book())

