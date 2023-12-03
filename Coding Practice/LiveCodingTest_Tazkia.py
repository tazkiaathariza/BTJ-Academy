'''
To Do List
Tazkia Athariza
Live Coding Test

Aplikasi untuk menambahkan task, mengubah status task,
menampilkan semua daftar task saat ini, menampilkan daftar task berdasarkan status task 
yang diinputkan, menghapus task, dan menampilkan persentase task yang telah selesai.

Data yang perlu disimpan pada aplikasi ini adalah: Nama Task, Prioritas Task [High/Low/Medium], Status Task [To Do/In Progress/Finished]

Catatan
1. Prioritas Task diinputkan ketika pengguna menambahkan task
2. Perubahan status harus sesuai urutan [To Do -> In Progress -> Finished], secara default, status task adalah To Do
'''

import json

# function 1
def add_task():
    activity = input("Add your task that needs to get done: ")
    priority = input("What's the priority of your task?[high/medium/low]: ")

    new_data = {
        "activity": activity,
        "priority": priority,
        "status": "To Do"
    }

    with open("todolist.txt", "a") as file:
        str_data = json.dumps(new_data) # mengubah data dictionary menjadi string
        file.write(str_data + '\n')
    
    print("New task already added successfully!")


# function 2
def view_alltask():
    print("This is your To Do List:")

    with open("todolist.txt", "r") as file:
        baris = file.readlines() # read per baris > jadi list
        for each_data in baris:
            dict_data = json.loads(each_data) # mengubah string menjadi dict
            print("Activity:", dict_data["activity"], "|", "Priority:", dict_data["priority"], "|", "Status:", dict_data["status"])


# function 3
def change_status():
    statustochange = input("Enter the name of activity that you want to change its status: ")

    with open("todolist.txt", "r") as file:
        
        baris = file.readlines()
        newtemp = []

        for each_data in baris:
            dict_data = json.loads(each_data)
            if dict_data["activity"] == statustochange: # cek nama activity
                if dict_data["status"] == "To Do": # pengkondisian status
                    dict_data["status"] = "In Progress" # mengganti to do jadi in progress
                elif dict_data["status"] == "In Progress":
                    dict_data["status"] = "Finished" # mengganti in progress jadi finished
                else:
                    dict_data["status"] = "Finished"
        
            newtemp.append(json.dumps(dict_data) + '\n')

        with open("todolist.txt", "w") as file:
            file.writelines(newtemp)
    
    print(f"The status for {statustochange} has been change")

# function 4
def view_statustask():
    taskstatus = input("Do you want to see your task based on what?(To Do, In Progress, Finished): ")
    print(f"Your {taskstatus} task:")

    with open("todolist.txt", "r") as file:
        baris = file.readlines()
        for each_data in baris:
            dict_data = json.loads(each_data) 
            if dict_data["status"] == taskstatus: # filter berdasarkan status
                print("Activity:", dict_data["activity"], "|", "Priority:", dict_data["priority"], "|", "Status:", dict_data["status"])

# function 5
def delete_task():
    delete_task = int(input("Which task do you want to delete? Enter NUMBER: "))

    with open("todolist.txt", "r") as file:
        baris = file.readlines()

    baris.pop(delete_task)

    with open("todolist.txt", "w") as file:
        file.writelines(baris)
    
    print("Task successfully deleted!")


# function 6
def finished_percent():
    print("Here's the percentage of task you already finished:")

    with open("todolist.txt", "r") as file:
        baris = file.readlines() # read per baris > jadi list
        totaltask = len(baris) # menghitung jumlah elemen
        finished = 0 # deklarasi awal jumlah task yang sudah selesai

        for each_data in baris:
            dict_data = json.loads(each_data) # mengubah string menjadi dict
            if dict_data["status"] == "Finished":
                finished += 1 # menambahkan yang sudah selesai
        
        percentage = finished/totaltask * 100 # perhitungan presentase

        print(percentage, "%")
              

# Menu
while True:
    print('\nWelcome! Menu:')
    print("1. Add new task in your list")
    print("2. View all of the task in your list")
    print("3. Change task status")
    print("4. View task list based on the status")
    print("5. Delete task based on the NUMBER (urutan list)")
    print("6. See how many task you already finished")
    print("7. Exit")

    decide = input("What do you decide?(1-7): ")

    if decide == "1":
        add_task()
    elif decide == "2":
        view_alltask()
    elif decide == "3":
        change_status()
    elif decide == "4":
        view_statustask()
    elif decide == "5":
        delete_task()
    elif decide == "6":
        finished_percent()
    elif decide == "7":
        print("Don't forget to do your task [EXITING]")
        break
    else:
        print("ERROR!")







