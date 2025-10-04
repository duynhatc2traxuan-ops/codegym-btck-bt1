import csv

def load_students(filename="students.csv"):
    students = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if "age" in row and row["age"].isdigit():
                    row["age"] = int(row["age"])
                else:
                    row["age"] = 0
                students.append(row)
    except FileNotFoundError:
        print("Chưa có file dữ liệu, bắt đầu với danh sách rỗng.")
    return students

def save_students(students, filename="students.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "name", "age", "major"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def add_student(students):
    student_id = input("Nhập ID sinh viên: ")
    for sv in students:
        if sv["id"] == student_id:
            print("ID đã tồn tại!")
            return
    name = input("Nhập họ tên: ")
    try:
        age = int(input("Nhập tuổi: "))
    except ValueError:
        print("Tuổi phải là số!")
        return
    major = input("Nhập ngành học: ")

    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "major": major
    })
    print("Đã thêm sinh viên thành công.")

def update_student(students):
    student_id = input("Nhập ID sinh viên cần cập nhật: ")
    for sv in students:
        if sv["id"] == student_id:
            print(f"Đang sửa thông tin của {sv['name']}")
            sv["name"] = input(f"Họ tên [{sv['name']}]: ") or sv["name"]
            try:
                new_age = input(f"Tuổi [{sv['age']}]: ")
                if new_age:
                    sv["age"] = int(new_age)
            except ValueError:
                print("Tuổi phải là số! Giữ nguyên giá trị cũ.")
            sv["major"] = input(f"Ngành học [{sv['major']}]: ") or sv["major"]
            print("Đã cập nhật thành công.")
            return
    print("Không tìm thấy sinh viên với ID này.")

def delete_student(students):
    student_id = input("Nhập ID sinh viên cần xóa: ")
    for sv in students:
        if sv["id"] == student_id:
            students.remove(sv)
            print("Đã xóa sinh viên.")
            return
    print("Không tìm thấy sinh viên với ID này.")

def search_student(students):
    keyword = input("Nhập tên cần tìm: ").lower()
    found = [sv for sv in students if keyword in sv["name"].lower()]
    if found:
        print("Kết quả tìm kiếm:")
        for sv in found:
            print(sv)
    else:
        print("Không tìm thấy sinh viên nào.")

def display_students(students):
    if not students:
        print("Danh sách trống.")
        return
    print(f"{'ID':<5}{'Name':<15}{'Age':<5}{'Major'}")
    print("-" * 40)
    for sv in students:
        print(f"{sv['id']:<5}{sv['name']:<15}{sv['age']:<5}{sv['major']}")

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

if __name__ == "__main__":
    menu()  