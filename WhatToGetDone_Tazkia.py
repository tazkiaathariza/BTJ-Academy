'''
Just a coding practice for manipulate data.
Tazkia
Case : Make a list containing dict data >> deadline hour + what to do
'''

import json

def add_list():
    activity = input("Enter the thing you need to get done: ") # input aktivitas
    time = input("Enter the deadline time: ") # input waktu

    new_data = {  # buat data list baru dalam bentuk dictionary
        "activity": activity, 
        "deadline_time": time,
        "status": False # pengguna belum mengerjakan aktivitas tersebut
    }

    with open("togetdone.txt" , "a") as file: #buka file dengan method "a" agar bisa menambahkan line baru
        str_data = json.dumps(new_data) # mengubah data dictionary menjadi string
        file.write(str_data + '\n')

    print("Activity list added successfully.")

def view_list():
    print("Your Notes:")
    
    with open("togetdone.txt", "r") as file:
        baris = file.readlines() # baca per baris, jadi bentuk list

        for each_data in baris: # looping buat print perbaris 1 1
            dict_data = json.loads(each_data) # mengubah string jd dictionary biar bisa direwrite :
            print("Activity:", dict_data["activity"], " | ", "Deadline:", dict_data["deadline_time"], " | ", "Status:", dict_data["status"])

def change_status():
    statustochange = input("Enter activity that you already get done: ")

    with open("togetdone.txt", "r") as file:
        baris = file.readlines()
        temp = []

        for each_data in baris:
            dict_data = json.loads(each_data)
            if dict_data["activity"] == statustochange:
                if  dict_data["status"] == False:
                    dict_data["status"] = True
                else:
                    dict_data["status"] = False

            temp.append(json.dumps(dict_data) + '\n')
        
        with open("togetdone.txt", "w") as file:
            file.writelines(temp)
    
    print("Change status successful.")

            

def delete_list():
    view_list() # Before
    want_deleted = int(input("Enter lines that you want to delete: "))

    with open("togetdone.txt", "r") as file:
        baris = file.readlines() # baca per baris, jadi bentuk list
    
    baris.pop(want_deleted)

    with open("togetdone.txt", "w") as file:
        file.writelines(baris)

    print(f"Note deleted successfully.")
    view_list() # After Delete

while True:
    print("\nMenu:")
    print("1. Add List on What To Get Done")
    print("2. View List of your Deadlines!")
    print("3. Delete List")
    print("4. Change Status")
    print("5. Exit")
   

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_list()
    elif choice == "2":
        view_list()
    elif choice == "3":
        delete_list()
    elif choice == "4":
        change_status()
    elif choice == "5":
        print("Exiting the Note App.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
