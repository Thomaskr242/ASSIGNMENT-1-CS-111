# library_manager.py
# Basic Library Manager
# Demonstrates variables, input/output, and basic calculation
###################################################################################################
def add_book(books, title, author, year, genre, read_status):
    """Add a new book to the library"""
    if not title or not author or not genre:
        print("Error: Title, author, and genre are required fields.")
        return
    if not (1000 <= year <= 2025):
        print("Error: Year must be between 1000 and the current year.")
        return
    for book in books:
        if book['title'].lower() == title.lower():
            print("Error: Duplicate title is not allowed.")
            return
    books.append({
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read_status': read_status
    })
    print(f"Book '{title}' added successfully.")

def remove_book(books, title):
    """Remove a book from the library by title"""
    for book in books:
        if book['title'].lower() == title.lower():
            books.remove(book)
            print(f"Book '{title}' removed successfully.")
            return
    print(f"Error: Book '{title}' not found.")

def mark_as_read(books, title):
    """Mark a book as read"""
    for book in books:
        if book['title'].lower() == title.lower():
            book['read_status'] = True
            print(f"Book '{title}' marked as read.")
            return
    print(f"Error: Book '{title}' not found.")

def get_books_by_author(books, author):
    """Return all books by a specific author"""
    result = [book for book in books if book['author'].lower() == author.lower()]
    if not result:
        print(f"No books found by author '{author}'.")
    return result

def calculate_statistics(books):
    """Calculate and display library statistics"""
    total_books = len(books)
    read_books = sum(1 for book in books if book['read_status'])
    unread_books = total_books - read_books
    books_by_genre = {}
    for book in books:
        genre = book['genre']
        books_by_genre[genre] = books_by_genre.get(genre, 0) + 1
    print(f"Total books: {total_books}")
    print(f"Read books: {read_books}")
    print(f"Unread books: {unread_books}")
    print("Books by genre:")
    for genre, count in books_by_genre.items():
        print(f"  {genre}: {count}")

def books_by_year(books, year, before=True):
    """Return books published before or after a given year"""
    if before:
        return [book for book in books if book['year'] < year]
    return [book for book in books if book['year'] >= year]

def main():
    library = []
    while True:
        print("\nLibrary Manager Options:")
        print("1. Add a new book")
        print("2. Remove a book")
        print("3. Mark a book as read")
        print("4. View all books")
        print("5. View statistics")
        print("6. Search for books by author")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            try:
                year = int(input("Enter publication year: ").strip())
            except ValueError:
                print("Error: Year must be a valid number.")
                continue
            genre = input("Enter genre: ").strip()
            read_status = input("Have you read this book? (yes/no): ").strip().lower() == 'yes'
            add_book(library, title, author, year, genre, read_status)
        elif choice == "2":
            title = input("Enter the title of the book to remove: ").strip()
            remove_book(library, title)
        elif choice == "3":
            title = input("Enter the title of the book to mark as read: ").strip()
            mark_as_read(library, title)
        elif choice == "4":
            if not library:
                print("No books in the library.")
            else:
                print("\nBooks in Library:")
                for book in library:
                    print(f"- {book['title']} by {book['author']} ({book['year']}, {book['genre']}) - {'Read' if book['read_status'] else 'Unread'}")
        elif choice == "5":
            calculate_statistics(library)
        elif choice == "6":
            author = input("Enter the author's name to search for: ").strip()
            books_by_author = get_books_by_author(library, author)
            if books_by_author:
                print(f"\nBooks by {author}:")
                for book in books_by_author:
                    print(f"- {book['title']} ({book['year']}, {book['genre']}) - {'Read' if book['read_status'] else 'Unread'}")
        elif choice == "7":
            print("Exiting Library Manager. SEEYA!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 7.")

# Run the program
if __name__ == "__main__":
    main()
