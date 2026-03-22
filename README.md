# 🎓 Student Grade Calculator

## 📌 Overview

The **Student Grade Calculator** is a Python-based application that processes multiple students' marks, calculates averages, assigns grades, and generates class statistics. It also includes features like input validation, search functionality, and file saving.

---

## 🚀 Features

* ✔ Processes multiple students
* ✔ Calculates grades using a custom grading system
* ✔ Provides personalized comments
* ✔ Displays formatted results in table form
* ✔ Calculates class statistics (average, highest, lowest with names)
* ✔ Input validation with error handling
* ✔ Search functionality for students
* ✔ Save results to a file
* ✔ Menu-driven interface

---

## ⚙️ Technologies Used

* Python (Core Concepts)
* Functions
* Lists & Dictionaries
* File Handling

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/week2-grade-calculator.git

# Navigate into the folder
cd week2-grade-calculator

# Run the program
python grade_calculator.py
```

---

## 🧪 Test Input (test_students.txt)

You can test the program using:

```bash
python grade_calculator.py < test_students.txt
```

---

## 📊 Grading System

| Grade | Marks Range | Comment                  |
| ----- | ----------- | ------------------------ |
| A     | 90–100      | Keep up the good work!   |
| B     | 80–89       | Good job!                |
| C     | 70–79       | You can do better!       |
| D     | 60–69       | You need to work harder! |
| F     | 0–59        | Consult a teacher!       |

---

## 📁 Sample Output

```
STUDENT RESULTS
------------------------------------------------------
Name           Avg       Grade     Comment
------------------------------------------------------
John           88.33     B         Good job!
Sarah          91.00     A         Keep up the good work!
------------------------------------------------------

Class Average: 89.67
Highest: 91.00 (Sarah)
Lowest: 88.33 (John)
```

---

## ⚠️ Error Handling

* Ensures valid numeric input
* Prevents invalid marks (outside 0–100)
* Handles incorrect menu choices

---

## 🔍 Search Feature

Users can search for a student by name (case-insensitive).

---

## 💾 File Saving

Results can be saved into `results.txt` for future reference.

---

## 📌 Future Improvements

* Add GUI (Tkinter / JavaFX)
* Export results to CSV
* Add ranking system
* Support more subjects

---

## 👩‍💻 Author

**Dhanushiya S**
