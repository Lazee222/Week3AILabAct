def check_borrowing(overdue_books, status):

    if overdue_books == "yes":
        return "Not allowed: overdue books"

    elif status == "suspended":
        return "Not allowed: suspended account"

    else:
        return "Borrowing allowed"


allowed_students = 0

while True:

    name = input("Enter student name (or 'exit' to stop): ").strip()

    if name.lower() == "exit":
        break

    overdue = input("Do you have overdue books? (yes/no): ").strip().lower()
    status = input("Enter status (active/suspended): ").strip().lower()
    books = int(input("How many books do you want to borrow? "))

    result = check_borrowing(overdue, status)

    if result == "Borrowing allowed":

        if books <= 0:
            print("Error: Please enter at least 1 book.")

        elif books > 3:
            print("You can only borrow up to 3 books.")
            print("Borrowing approved for 3 books.")
            allowed_students += 1

        else:
            print("Borrowing approved for", books, "book(s).")
            allowed_students += 1

    else:
        print(result)

    print()

print("Total students allowed to borrow:", allowed_students)
