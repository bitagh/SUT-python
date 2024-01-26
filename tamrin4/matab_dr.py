class Clinic:
    _patients = dict()
    _visits = dict()

    def __init__(self, id, name, last_name, age, height, weight):
        _add_flag = True

        self.id = int(id)
        self.name = name
        self.last_name = last_name
        self.age = int(age)
        self.height = int(height)
        self.weight = int(weight)

        if self._is_patient_valid(self.id):
            print("error: this ID already exists")
            _add_flag = False

        if self.age < 0 and _add_flag:
            print("error: invalid age")
            _add_flag = False

        if self.height < 0 and _add_flag:
            print("error: invalid height")
            _add_flag = False

        if self.weight < 0 and _add_flag:
            print("error: invalid weight")
            _add_flag = False

        if _add_flag:
            Clinic._patients[self.id] = [self.name,
                                         self.last_name,
                                         self.age,
                                         self.height,
                                         self.weight
                                         ]
            print("patient added successfully")

    @classmethod
    def add_patient(cls, id, name, last_name, age, height, weight):
        return cls(id, name, last_name, age, height, weight)

    @staticmethod
    def delete_patient(id):
        id = int(id)
        ret = Clinic._patients.pop(id, None)
        if ret is None:
            print("error: invalid id")
        else:
            Clinic._visits = {visit_time: patient_id for visit_time, patient_id in Clinic._visits.items() if patient_id != id}
            print("patient deleted successfully!")

    @staticmethod
    def add_visit(id, visit_time):
        _add_flag = True
        id = int(id)
        visit_time = int(visit_time)

        if not Clinic._is_patient_valid(id):
            print("error: invalid id")
            _add_flag = False

        if not 9 <= visit_time <= 18 and _add_flag:
            print("error: invalid time")
            _add_flag = False

        if visit_time in Clinic._visits.values() and _add_flag:
            print("error: busy time")
            _add_flag = False

        if _add_flag:
            Clinic._visits[visit_time] = id
            print("visit added successfully!")

    @staticmethod
    def patient_display(id):
        id = int(id)
        if Clinic._is_patient_valid(id):
            p = Clinic._patients[id]
            print(f"patient name: {p[0]}")
            print(f"patient family name: {p[1]}")
            print(f"patient age: {p[2]}")
            print(f"patient height: {p[3]}")
            print(f"patient weight: {p[4]}")
        else:
            print("error: invalid ID")

    @staticmethod
    def visit_display():
        print("SCHEDULE:")
        for visit_time, patient_id in Clinic._visits.items():
            p = Clinic._patients[patient_id]
            print(f"{visit_time}:00 {p[0]} {p[1]}")

    @staticmethod
    def _is_patient_valid(id):
        return id in Clinic._patients

    @staticmethod
    def _is_visit_valid(time):
        return time in Clinic._visits


while True:
    cmd = input('').split(' ')

    for idx, word in enumerate(cmd):
        if word == "add":
            if cmd[idx + 1] == "patient":
                Clinic.add_patient(*cmd[idx + 2:])
            elif cmd[idx + 1] == "visit":
                Clinic.add_visit(*cmd[idx + 2:])
            else:
                print("invalid command")
            break

        elif word == "display":
            if cmd[idx + 1] == "patient":
                Clinic.patient_display(*cmd[idx + 2:])
            elif cmd[idx + 1] == "visit" and cmd[idx + 2] == "list":
                Clinic.visit_display()
            else:
                print("invalid command")
            break

        elif word == "delete":
            Clinic.delete_patient(*cmd[idx + 2:])
            break

        elif word == "exit":
            exit()

        else:
            print("invalid command")
            break
