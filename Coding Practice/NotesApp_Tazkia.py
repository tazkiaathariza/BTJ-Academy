'''
Latihan Coding - Python - Pertemuan 6 BTJ Academy
Tazkia Athariza
Case : Notes App || File Manipulation
'''


def add_note():
    note = input("Enter your note: ")

    note_app = "notesapp.txt"
    with open(note_app, "a") as notes: # menggunakan "with" agar otomatis closed dan "a" agar tidak menghapus isi file
        notes.write(note + '\n') # \n for enter
    
    print("Note added successfully.") # notifikasi

def view_notes():
    print("Your Notes:")

    note_app = "notesapp.txt"
    with open(note_app, "r") as notes:
        isi_notes = notes.read()
        print(isi_notes)

def delete_note():
    view_notes() # Before
    deleted = input("Enter the number of the note to delete: ")
    deletedint = int(deleted) # mengubah string menjadi integer

    note_app = "notesapp.txt"
    with open(note_app, "r") as notes:
        baris = notes.readlines() # membaca per baris

    baris.pop(deletedint) # menghapus line yang diinginkan

    with open(note_app, "w") as notes: # menuliskan kembali baris setelah ada yang dihapus
        notes.writelines(baris)

    print(f"Note deleted successfully.")
    view_notes() # After Delete

while True:
    print("\nMenu:")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        print("Exiting the Note App.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
