import sqlite3

class ClinicDB:
    def __init__(self, db_name="clinic.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patient (
                Patient_ID INTEGER PRIMARY KEY,
                patient_fullname TEXT NOT NULL,
                patient_address TEXT NOT NULL,
                patient_phone TEXT NOT NULL,
                patient_age INTEGER NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Doctor (
                Doctor_ID INTEGER PRIMARY KEY,
                doctor_fullname TEXT NOT NULL,
                doctor_specialisation TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Appointment (
                Appointment_ID INTEGER PRIMARY KEY,
                Appointment_date DATE NOT NULL,
                Appointment_time TEXT NOT NULL,
                Patient_ID INTEGER,
                Doctor_ID INTEGER,
                FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
                FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID)
            )
        """)

        self.conn.commit()

    def insert_sample_data(self):
        patients = [
            (1, "Ram Sharma", "Nepal", "9800000001", 75),
            (2, "Sita Adhikari", "India", "9800000002", 70),
            (3, "Amit Karki", "Hwai", "9800000003", 25)
        ]

        doctors = [
            (1, "Dr. Anil Thapa", "Ophthalmology", "9876780234"),
            (2, "Dr. Bina Shrestha", "Cardiology", "9875432455"),
            (3, "Dr. Ramesh KC", "Ophthalmology", "9843456345")
        ]

        appointments = [
            (1, "2025-12-01", "12:00", 1, 1),
            (2, "2025-12-02", "11:40", 2, 3),
            (3, "2025-12-03", "01:05", 3, 2)
        ]

        self.cursor.executemany(
            "INSERT OR IGNORE INTO Patient VALUES (?, ?, ?, ?, ?)", patients
        )
        self.cursor.executemany(
            "INSERT OR IGNORE INTO Doctor VALUES (?, ?, ?, ?)", doctors
        )
        self.cursor.executemany(
            "INSERT OR IGNORE INTO Appointment VALUES (?, ?, ?, ?, ?)", appointments
        )

        self.conn.commit()

    # 1. list Senior patients (>65)
    def list_senior_patients(self):
        self.cursor.execute("""
            SELECT * FROM Patient
            WHERE patient_age > 65
        """)
        return self.cursor.fetchall()

    #  Ophthalmology doctor count
    def count_ophthalmology_doctors(self):
        self.cursor.execute("""
            SELECT COUNT(*) FROM Doctor
            WHERE doctor_specialisation = 'Ophthalmology'
        """)
        return self.cursor.fetchone()[0]

    def close(self):
        self.conn.close()


# Main Program
if __name__ == "__main__":
    clinic = ClinicDB()
    clinic.insert_sample_data()

    print("Senior Patients (Age > 65):")
    for p in clinic.list_senior_patients():
        print(p)

    print("\nTotal Ophthalmology Doctors:",
          clinic.count_ophthalmology_doctors())

    clinic.close()
