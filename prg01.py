from datetime import datetime, date

class Student:
    def __init__(self, name: str, dob: str):
        self.name = name
        self.dob = self.parse_dob(dob)

    def parse_dob(self, dob: str) -> date:
        for fmt in ("%d-%m-%Y", "%Y-%m-%d"):
            try:
                return datetime.strptime(dob, fmt).date()
            except ValueError:
                continue
        raise ValueError("Date of birth format should be DD-MM-YYYY or YYYY-MM-DD")

    def calculate_age(self) -> int:
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.calculate_age()}")

class StudentCourses:
    def __init__(self):
        self.semesters = {}

    def add_course(self, semester: str, course_name: str, marks: int):
        if semester not in self.semesters:
            self.semesters[semester] = []
        self.semesters[semester].append((course_name, marks))

    def display_courses(self):
        for sem, courses in self.semesters.items():
            print(f"Semester: {sem}")
            for course, marks in courses:
                print(f"  Course: {course}, Marks: {marks}")
if __name__ == "__main__":
    student = Student("Alice", "2003-04-15")
    student.display()

    courses = StudentCourses()
    courses.add_course("Semester 1", "Math", 85)
    courses.add_course("Semester 1", "Physics", 78)
    courses.add_course("Semester 2", "Chemistry", 92)
    courses.display_courses()