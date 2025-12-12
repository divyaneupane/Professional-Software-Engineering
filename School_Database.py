import sqlite3

class SchoolDB:
    def __init__(self,db_name='schooldatabase.db'):
        #connect to Sqlite database
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
        self.create_tables()
        
        
        
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Student(
                 Student_ID INTEGER PRIMARY KEY,
                S_Firstname VARCHAR(20) NOT NULL, 
                S_Lastname VARCHAR(20) NOT NULL, 
                DOB DATE NOT NULL       
            )
        ''')

# Create Teacher Table  
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Teacher(
                T_ID INTEGER PRIMARY KEY,
                T_FirstName VARCHAR(20) NOT NULL,
                T_LastName VARCHAR(20) NOT NULL,
                T_email VARCHAR(50) NOT NULL
            )
        ''')

# Create Course Table  
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Course(
                C_ID TEXT PRIMARY KEY,
                C_Name VARCHAR(30) NOT NULL,
                C_Time TEXT NOT NULL
            )
        ''')

# Enroll Table (Student -> Course)  
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Enroll(
                Student_ID INTEGER,
                C_ID TEXT,
                FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
                FOREIGN KEY (C_ID) REFERENCES Course(C_ID)
            )
        ''')

# Delivers Table (Teacher -> Course)  
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Delivers(
                T_ID INTEGER,
                C_ID TEXT,
                FOREIGN KEY (T_ID) REFERENCES Teacher(T_ID),
                FOREIGN KEY (C_ID) REFERENCES Course(C_ID)
            )
        ''')
        self.conn.commit()   #save all changes into database permanently
        
    
    def insert_data(self):
        
    # Insert Student Data
        Students = [
            (101, "Divya", "Neupane", "2001-05-15"),
            (102, "Dikshya", "Neupane", "2005-07-28"),
        ]
        #insert into table
        self.cursor.executemany("INSERT INTO Student VALUES (?, ?, ?, ?)", Students)

        # Teacher Data
        Teachers = [
            (1001, "Anny", "Sharma", "anny@gmail.com"),
            (1002, "Sabita", "Shahi", "sabita@gmail.com"),
        ]
        #insert into table
        self.cursor.executemany("INSERT INTO Teacher VALUES (?, ?, ?, ?)", Teachers)
        
        # Course Data
        Courses = [
            ("MSE800", "Professional Software Engineering", "10 weeks"),
            ("MSE801", "Quantum Computing", "10 weeks")
        ]
        #insert into table
        self.cursor.executemany("INSERT INTO Course VALUES (?, ?, ?)", Courses)


        # Enrollment Data 
        Enroll= [
            (101, "MSE800"),
            (102, "MSE801")  
        ]
        #insert into table
        self.cursor.executemany("INSERT INTO Enroll VALUES (?, ?)", Enroll)
        
        
        # Deliver Data
        Delivers = [
            (1001, "MSE800"),
            (1002, "MSE801")
        ]
        #insert into table
        self.cursor.executemany("INSERT INTO Delivers VALUES (?, ?)", Delivers)



    #to count students for a specific course
    def count_students(self,C_ID):
        self.cursor.execute(
            "SELECT COUNT(*) FROM ENROLL WHERE C_ID = ?",(C_ID,) 
        )
        count=self.cursor.fetchone()[0]  #fetch the results
        return count
    
        # to list all teachers teaching a specific course
    def list_teachers(self, C_ID):
        self.cursor.execute('''
            SELECT T_FirstName, T_LastName
            FROM Teacher t
            JOIN Delivers d ON t.T_ID = d.T_ID
            WHERE d.C_ID = ?
        ''', (C_ID,))
        
        teachers = self.cursor.fetchall()  # fetch all rows
        return [f"{t[0]} {t[1]}" for t in teachers]  # format names

   
   
#Main program section 
if __name__ == "__main__":
    db = SchoolDB()        # create database
    db.insert_data()       # insert sample data

    # show number of students in MSE800
    total = db.count_students("MSE800")
    print(f"Number of students in MSE800: {total}")

    # list teachers teaching MSE801
    teachers = db.list_teachers("MSE801")
    print("Teachers teaching MSE801:")
    for t in teachers:
        print(t)

    db.conn.close()        # close connection
