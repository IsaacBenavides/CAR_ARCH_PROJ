from datetime import datetime


class StudentEntity:
    def __init__(self, student) -> None:
        self._errors = []
        self.student = student
        self.name = self.get_name()
        self.last_name = self.get_last_name()
        self.date_of_birth = self.get_date_of_birth()
        self.gender = self.get_gender()
        self.age = self.get_age()
        self.phone = self.get_phone()
        self.date_of_admition = self.get_date_of_admition()
        self.admition_status = self.get_admition_status()
        self.email = self.get_email()

    def get_name(self):
        try:
            return self.get("Nombre")
        except Exception as e:
            self._errors.append(e)

    def get_last_name(self):
        try:
            return self.get("Apellido")
        except Exception as e:
            self._errors.append(e)

    def get_date_of_birth(self):
        try:
            date = datetime.fromtimestamp(self.get("Fecha de Nacimiento") / 1e3)
            return date
        except Exception as e:
            print(e)
            self._errors.append(e)

    def get_gender(self):
        try:
            return self.get("Genero")
        except Exception as e:
            self._errors.append(e)

    def get_age(self):
        try:
            age = self.get("Edad")
            return int(age)
        except Exception as e:
            self._errors.append(e)

    def get_phone(self):
        try:
            phone = self.get("Teléfono")
            return f"+57{int(phone)}"
        except Exception as e:
            self._errors.append(e)

    def get_date_of_admition(self):
        try:
            date = datetime.fromtimestamp(self.get("Fecha de Admisión") / 1e3)
            return date
        except Exception as e:
            self._errors.append(e)

    def get_admition_status(self):
        try:
            return self.get("Estado Matricula")
        except Exception as e:
            self._errors.append(e)

    def get_email(self):
        try:
            return self.get("email")
        except Exception as e:
            self._errors.append(e)

    def get(self, field):
        value = self.student.get(field)
        if value == None:
            raise EmptyField(value)
        return value

    def to_string(self):
        return f"Nombre: {self.name}, Apellido: {self.last_name}, Fecha de Nacimiento: {self.date_of_birth}, Edad: {self.age}, Genero: {self.gender}, Teléfono: {self.phone}, Fecha de Admisión: {self.date_of_admition}, Estado matricula: {self.admition_status}, Email: {self.email}"

    def has_errors(self):
        return len(self._errors) != 0


class EmptyField(Exception):
    def __init__(self, field):
        self.message = f"{field} is Empty"
