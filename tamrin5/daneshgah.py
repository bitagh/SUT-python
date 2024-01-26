import re

class User:
    def __init__(self, user_id, name, password):
        self.id = user_id
        self.name = name
        self.password = password

class Student(User):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)
        self.courses = set()

class Professor(User):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)
        self.courses_taught = set()

class Course:
    def __init__(self, course_id, name, capacity):
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.current_students = set()

class MainApp:
    def __init__(self):
        self.users = {}
        self.courses = {}
        self.commands = []
        self.poin = 0

    def sign_up(self, user_type, user_id, name, password):
        if user_type not in {"S", "P"}:
            print("invalid type")
            return
        if not user_id.isdigit():
            print("invalid id")
            return
        if " " in name:
            print("invalid name")
            return
        if not (4 <= len(password) <= 20 and any(c in "*!@$%^&()" for c in password)):
            print("invalid password")
            return
        if user_id in self.users:
            print("id already exists")
            return
        if user_type == "S":
            print("signed up successfully!")
            self.users[user_id] = Student(user_id, name, password)
        elif user_type == "P":
            print("signed up successfully!")
            self.users[user_id] = Professor(user_id, name, password)

    def log_in(self, user_id, password):
        if user_id not in self.users:
            print("incorrect id")
            return
        user = self.users[user_id]

        if user.password != password:
            print("incorrect password")
            return

        if isinstance(user, Student):
            print("logged in successfully!\nentered student menu")
            self.student_menu(user)
        elif isinstance(user, Professor):
            print("logged in successfully!\nentered professor menu")
            self.professor_menu(user)

    def student_menu(self, student):
        while True:
            self.poin += 1
            command = self.commands[self.poin]
            if command == "edu log out edu":
                print("logged out successfully!")
                print("entered log in/sign up menu")
                return
            elif command == "edu show course list edu":
                self.show_course_list()
            elif command.startswith("edu get course -i "):
                course_id = command.split()[-2]
                self.get_course(student, course_id)
            elif command == "edu current menu edu":
                print("student menu")
            else:
                print("invalid command")

    def professor_menu(self, professor):
        while True:
            self.poin += 1
            command = self.commands[self.poin]
            if command == "edu log out edu":
                print("logged out successfully!")
                print("entered log in/sign up menu")
                return
            elif command == "edu show course list edu":
                self.show_course_list()
            elif command.startswith("edu add course -c "):
                match = re.match(r'^edu add course -c (.+?) -i (.+?) -n (.+?) edu$', command)
                if match:
                    course_name, course_id, capacity = match.groups()
                    self.add_course(professor, course_id, course_name, capacity)
                else:
                    print("Invalid command")
            elif command == "edu current menu edu":
                print("professor menu")
            else:
                print("invalid command")

    def show_course_list(self):
        print("course list:")
        for course in self.courses.values():
            print(f"{course.course_id} {course.name} {len(course.current_students)}/{course.capacity}")

    def get_course(self, student, course_id):
        if course_id not in self.courses:
            print("incorrect course id")
            return

        course = self.courses[course_id]

        if student in course.current_students:
            print("you already have this course")
        elif len(course.current_students) >= course.capacity:
            print("course is full")
        else:
            course.current_students.add(student)
            print("course added successfully!")

    def add_course(self, professor, course_id, course_name, capacity):
        if course_id in self.courses:
            print("course id already exists")
            return

        self.courses[course_id] = Course(course_id, course_name, int(capacity))
        print("course added successfully!")

    def main(self):
        while True:
            try:
                line = input().strip()
                if line == 'edu exit edu':
                    break
                self.commands.append(line)
            except EOFError:
                break

        while True:
            if self.poin == len(self.commands):
                break
            command = self.commands[self.poin]
            if command == "edu exit edu":
                break
            elif command == "edu current menu edu":
                print("log in/sign up menu")
            elif command.startswith("edu sign up -"):
                match = re.match(r'^edu sign up -(.+?) -i (.+?) -n (.+?) -p (.+?) edu$', command)
                if match:
                    user_type, user_id, name, password = match.groups()
                    self.sign_up(user_type, user_id, name, password)
                else:
                    print("invalid command")
                    self.poin += 1
                    continue
            elif command.startswith("edu log in -"):
                match = re.match(r'^edu log in -i (.+?) -p (.+?) edu$', command)
                if match:
                    user_id, password = match.groups()
                else:
                    print("invalid command")
                    self.poin += 1
                    continue

                self.log_in(user_id, password)
            else:
                print("invalid  command")
            self.poin += 1


if __name__ == "__main__":
    app = MainApp()
    app.main()
