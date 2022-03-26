# Project 1 : basic school administration tool
# Project 1 (file 1)
import csv
from tkinter.messagebox import YES


def write(self):
    with open("student_info.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Phone No.", "Email"])
        writer.writerow(self)


def read():
    import csv
    with open('student_info.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print('\n', row)


if __name__ == "__main__":
    std_num = 0
    new_std = input("Do you want to add a new student's info ? yes/no ")
    while new_std == "yes":
        student_info = input("\nEnter student's name , age , number, email:  ")
        student_info_list = student_info.split(", ")
        print("\nEntered info is - \nName: {}\nAge: {}\nPhone No.: {}\nEmail: {}"
            .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        choice_check = input("\nIs the entered info correct: yes/no: ")
        if choice_check == "yes":
            write(student_info_list)
            std_num += 1
        else:
            print("Re_enter info : ")
            continue
        condition_check = input("\nDo you want to another Student's info: yes/no ")
        if condition_check == "no":
            new_std = "no"

    print("\nNew students added in list ", std_num)
    read()
