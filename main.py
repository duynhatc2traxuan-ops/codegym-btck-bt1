import csv

def load_students(filename="output.csv"):
    students = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["age"] = int(row["age"])
                students.append(row)
    except FileNotFoundError:
        print("Chưa có file dữ liệu, bắt đầu với danh sách rỗng.")
    return students

def save_students(students, filename="output.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "name", "age", "major"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def add_student(students):
    print(students)

def update_student(students):
    print(students)

def delete_student(students):
    print(students)

def search_student(students):
    print(students)

def display_students(students):
    print(students)

def menu():
    students = load_students()

    while True:
        print("\n===== MENU QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Cập nhật sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên theo tên")
        print("5. Hiển thị danh sách sinh viên")
        print("6. Lưu & Thoát")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            search_student(students)
        elif choice == "5":
            display_students(students)
        elif choice == "6":
            save_students(students)
            print("Đã lưu dữ liệu. Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

  