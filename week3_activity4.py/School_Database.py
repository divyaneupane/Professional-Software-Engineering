import sqlite3

class SchoolDB:
    def __init__(self, db_name='schooldatabase.db'):
        # Connect to SQLite database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Student table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Student(
                Student_ID INTEGER PRIMARY KEY,
                S_Firstname VARCHAR(20) NOT NULL,
                S_Lastname VARCHAR(20) NOT NULL,
                DOB DATE NOT NULL
            )
        ''')

        # Teacher table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Teacher(
                T_ID INTEGER PRIMARY KEY,
                T_FirstName VARCHAR(20) NOT NULL,
                T_LastName VARCHAR(20) NOT NULL,
                T_email VARCHAR(50) NOT NULL
            )
        ''')

        # Course table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Course(
                C_ID TEXT PRIMARY KEY,
                C_Name VARCHAR(30) NOT NULL,
                C_Time TEXT NOT NULL
            )
        ''')

        # Enroll table (Student → Course)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Enroll(
                Student_ID INTEGER,
                C_ID TEXT,
                FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
                FOREIGN KEY (C_ID) REFERENCES Course(C_ID)
            )
        ''')

        # Delivers table (Teacher → Course)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Delivers(
                T_ID INTEGER,
                C_ID TEXT,
                FOREIGN KEY (T_ID) REFERENCES Teacher(T_ID),
                FOREIGN KEY (C_ID) REFERENCES Course(C_ID)
            )
        ''')

        self.conn.commit()

    def insert_data(self):
        # Clear existing data (avoids duplicate primary key errors)
        self.cursor.execute("DELETE FROM Enroll")
        self.cursor.execute("DELETE FROM Delivers")
        self.cursor.execute("DELETE FROM Student")
        self.cursor.execute("DELETE FROM Teacher")
        self.cursor.execute("DELETE FROM Course")

        # Insert students
        students = [
            (104, "Shila", "Sap", "1990-02-10"),
            (105, "Sita", "Neue", "2007-09-28")
        ]
        self.cursor.executemany(
            "INSERT INTO Student VALUES (?, ?, ?, ?)", students
        )

        # Insert teachers
        teachers = [
            (1003, "Anu", "Leoa", "anu@gmail.com"),
            (1004, "Sabi", "Lai", "sabi@gmail.com")
        ]
        self.cursor.executemany(
            "INSERT INTO Teacher VALUES (?, ?, ?, ?)", teachers
        )

        # Insert courses
        courses = [
            ("MSE800", "Professional Software Engineering", "10 weeks"),
            ("MSE801", "Quantum Computing", "10 weeks")
        ]
        self.cursor.executemany(
            "INSERT INTO Course VALUES (?, ?, ?)", courses
        )

        # Insert enrollments
        enrollments = [
            (104, "MSE800"),
            (105, "MSE801")
        ]
        self.cursor.executemany(
            "INSERT INTO Enroll VALUES (?, ?)", enrollments
        )

        # Insert course deliveries
        delivers = [
            (1003, "MSE800"),
            (1004, "MSE801")
        ]
        self.cursor.executemany(
            "INSERT INTO Delivers VALUES (?, ?)", delivers
        )

        self.conn.commit()

    # Count students for a specific course
    def count_students(self, C_ID):
        self.cursor.execute(
            "SELECT COUNT(*) FROM Enroll WHERE C_ID = ?", (C_ID,)
        )
        return self.cursor.fetchone()[0]

    # List teachers teaching a specific course
    def list_teachers(self, C_ID):
        self.cursor.execute('''
            SELECT T_FirstName, T_LastName
            FROM Teacher t
            JOIN Delivers d ON t.T_ID = d.T_ID
            WHERE d.C_ID = ?
        ''', (C_ID,))
        return [f"{t[0]} {t[1]}" for t in self.cursor.fetchall()]


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    db = SchoolDB()        # Create database and tables
    db.insert_data()       # Insert sample data

    # Display number of students in MSE800
    total = db.count_students("MSE800")
    print(f"Number of students in MSE800: {total}")

    # Display teachers teaching MSE801
    teachers = db.list_teachers("MSE801")
    print("Teachers teaching MSE801:")
    for teacher in teachers:
        print(teacher)

    db.conn.close()
