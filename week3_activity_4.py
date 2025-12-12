"""
Week 3 - Activity 4
SQLite3 OOP Project
Matches ERD provided (Student–Course–Teacher relationships)

- Creates database using sqlite3
- Creates tables based on ER diagram
- Inserts sample data
- Shows:
    1. Number of students enrolled in MSE800
    2. List of teachers delivering MSE801
"""

import sqlite3


# =============================
# Database Wrapper Class
# =============================

class Database:
    """Simple OOP wrapper for sqlite3 connection."""
    def __init__(self, db_name="school.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()

    def execute(self, sql, params=()):
        """Execute SQL (INSERT/UPDATE/DELETE)."""
        self.cur.execute(sql, params)
        self.conn.commit()

    def fetchall(self, sql, params=()):
        """Fetch multiple rows."""
        self.cur.execute(sql, params)
        return self.cur.fetchall()

    def fetchone(self, sql, params=()):
        """Fetch single row."""
        self.cur.execute(sql, params)
        return self.cur.fetchone()

    def close(self):
        self.conn.close()


# =============================
# University Database Manager
# =============================

class UniversityDB:
    """Handles table creation, inserts, and required queries."""
    def __init__(self):
        self.db = Database()

    # ------------------------
    # Create Tables
    # ------------------------
    def create_tables(self):
        """Creates all tables based on the ERD."""
        self.db.execute("PRAGMA foreign_keys = ON;")

        # Drop tables if they exist
        self.db.execute("DROP TABLE IF EXISTS Enrollment;")
        self.db.execute("DROP TABLE IF EXISTS Teaching;")
        self.db.execute("DROP TABLE IF EXISTS Student;")
        self.db.execute("DROP TABLE IF EXISTS Course;")
        self.db.execute("DROP TABLE IF EXISTS Teacher;")

        # STUDENT TABLE
        self.db.execute("""
        CREATE TABLE Student (
            Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            S_FirstName TEXT,
            S_LastName TEXT,
            DOB DATE
        );
        """)

        # COURSE TABLE
        self.db.execute("""
        CREATE TABLE Course (
            C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            C_Name TEXT,
            credit TIME
        );
        """)

        # TEACHER TABLE
        self.db.execute("""
        CREATE TABLE Teacher (
            T_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            T_FirstName TEXT,
            T_LastName TEXT,
            T_email TEXT
        );
        """)

        # ENROLLMENT TABLE (Student ↔ Course)
        self.db.execute("""
        CREATE TABLE Enrollment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Student_ID INTEGER,
            C_ID INTEGER,
            FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
            FOREIGN KEY (C_ID) REFERENCES Course(C_ID)
        );
        """)

        # TEACHING TABLE (Teacher ↔ Course)
        self.db.execute("""
        CREATE TABLE Teaching (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            T_ID INTEGER,
            C_ID INTEGER,
            FOREIGN KEY (T_ID) REFERENCES Teacher(T_ID),
            FOREIGN KEY (C_ID) REFERENCES Course(C_ID)
        );
        """)

    # ------------------------
    # Insert Methods
    # ------------------------
    def add_student(self, fname, lname, dob):
        self.db.execute(
            "INSERT INTO Student (S_FirstName, S_LastName, DOB) VALUES (?, ?, ?);",
            (fname, lname, dob)
        )

    def add_course(self, name, credit):
        self.db.execute(
            "INSERT INTO Course (C_Name, credit) VALUES (?, ?);",
            (name, credit)
        )

    def add_teacher(self, fname, lname, email):
        self.db.execute(
            "INSERT INTO Teacher (T_FirstName, T_LastName, T_email) VALUES (?, ?, ?);",
            (fname, lname, email)
        )

    def enroll(self, student_id, course_id):
        self.db.execute(
            "INSERT INTO Enrollment (Student_ID, C_ID) VALUES (?, ?);",
            (student_id, course_id)
        )

    def assign_teacher(self, teacher_id, course_id):
        self.db.execute(
            "INSERT INTO Teaching (T_ID, C_ID) VALUES (?, ?);",
            (teacher_id, course_id)
        )

    # ------------------------
    # Required Queries
    # ------------------------

    def count_students_in_course(self, course_name):
        """Return number of students enrolled in given course."""
        row = self.db.fetchone("""
        SELECT COUNT(*) AS total
        FROM Enrollment e
        JOIN Course c ON e.C_ID = c.C_ID
        WHERE c.C_Name = ?;
        """, (course_name,))

        return row["total"]

    def teachers_for_course(self, course_name):
        """Return list of teachers delivering a course."""
        rows = self.db.fetchall("""
        SELECT t.T_FirstName, t.T_LastName
        FROM Teaching tg
        JOIN Teacher t ON tg.T_ID = t.T_ID
        JOIN Course c ON tg.C_ID = c.C_ID
        WHERE c.C_Name = ?;
        """, (course_name,))

        return [(r["T_FirstName"], r["T_LastName"]) for r in rows]


# =============================
# Sample Data + Execution
# =============================

def main():
    uni = UniversityDB()
    uni.create_tables()

    # Insert courses
    uni.add_course("MSE800", "12:00")
    uni.add_course("MSE801", "14:00")

    # Insert teachers
    uni.add_teacher("Alice", "Smith", "alice@school.com")
    uni.add_teacher("Bob", "Kumar", "bob@school.com")

    # Insert students
    uni.add_student("Divya", "Neupane", "2004-02-18")
    uni.add_student("John", "Doe", "2003-11-02")

    # Enrollment (2 students in MSE800)
    uni.enroll(1, 1)
    uni.enroll(2, 1)

    # Teacher assignment (2 teachers for MSE801)
    uni.assign_teacher(1, 2)
    uni.assign_teacher(2, 2)

    # Required Output
    print("\nStudents in MSE800:", uni.count_students_in_course("MSE800"))
    print("\nTeachers delivering MSE801:")
    for t in uni.teachers_for_course("MSE801"):
        print(" -", t[0], t[1])


if __name__ == "__main__":
    main()
