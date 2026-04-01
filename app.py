def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note added!\n")


def view_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            if not notes:
                print("No notes found.\n")
            else:
                print("\nYour Notes:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
                print()
    except FileNotFoundError:
        print("No notes file found.\n")


def delete_note():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()

        view_notes()
        num = int(input("Enter note number to delete: "))

        if 1 <= num <= len(notes):
            notes.pop(num - 1)
            with open("notes.txt", "w") as f:
                f.writelines(notes)
            print("Note deleted!\n")
        else:
            print("Invalid number\n")

    except:
        print("Error deleting note\n")


def main():
    while True:
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    main()
