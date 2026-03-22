#Student Grade Calculator
#Author : Dhanushiya S

#Function to calculate the grade based on the score
def calculate_grade(score): 
    if score >= 90:
        return 'A', 'Keep up the good work!'
    elif score >= 80:
        return 'B', 'Good job!'
    elif score >= 70:
        return 'C', 'You can do better!'
    elif score >= 60:
        return 'D', 'You need to work harder!'
    else:
        return 'F', 'Consult a teacher!'
    
# Input validation for integer
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Enter a positive number.")
        except ValueError:
            print("Error: Invalid input. Enter a number.")

# Input validation for marks
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Error: Marks must be between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Enter numeric value.")

# Collect student data
def collect_data():
    num_students = get_positive_integer("Enter number of students: ")

    students = []

    for i in range(num_students):
        print(f"\n--- Student {i+1} ---")
        name = input("Enter student name: ")

        m1 = get_valid_marks("Subject 1")
        m2 = get_valid_marks("Subject 2")
        m3 = get_valid_marks("Subject 3")

        avg = (m1 + m2 + m3) / 3
        grade, comment = calculate_grade(avg)

        students.append({
            "name": name,
            "marks": [m1, m2, m3],
            "average": avg,
            "grade": grade,
            "comment": comment
        })

    return students

# Display results
def display_results(students):
    if not students:
        print("Warning: No data available.")
        return

    print("\nSTUDENT RESULTS")
    print("-" * 70)
    print(f"{'Name':<15}{'Avg':<10}{'Grade':<10}{'Comment':<20}")
    print("-" * 70)

    for s in students:
        print(f"{s['name']:<15}{s['average']:<10.2f}{s['grade']:<10}{s['comment']:<20}")

    print("-" * 70)

       # Class statistics
    averages = [s["average"] for s in students]

    class_avg = sum(averages) / len(averages)

    # Find highest and lowest student
    highest_student = max(students, key=lambda x: x["average"])
    lowest_student = min(students, key=lambda x: x["average"])

    print(f"\nClass Average: {class_avg:.2f}")
    print(f"Highest: {highest_student['average']:.2f} ({highest_student['name']})")
    print(f"Lowest: {lowest_student['average']:.2f} ({lowest_student['name']})")

# Search student
def search_student(students):
    name = input("Enter student name to search: ").lower()

    for s in students:
        if s["name"].lower() == name:
            print("\nStudent Found:")
            print(s)
            return

    print("Error: Student not found.")

# Save to file
def save_to_file(students):
    with open("results.txt", "w") as file:
        for s in students:
            file.write(f"{s}\n")

    print("Results saved to results.txt")


# Menu system
def menu():
    students = []

    while True:
        print("\n===== MENU =====")
        print("1. Enter Student Data")
        print("2. Display Results")
        print("3. Search Student")
        print("4. Save to File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            students = collect_data()
        elif choice == "2":
            display_results(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            save_to_file(students)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Error: Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    menu()