class Common:
    """
        Common base class for all Classes
    """
    count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Common.count += 1

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def profile_details(self):
        data = {
            "name": self.full_name()
        }
        return data


class Student(Common):

    def __init__(self, first_name, last_name, marks):
        super().__init__(first_name, last_name)
        self.marks = marks

    def profile_details(self):
        data = super().profile_details()
        data['marks'] = self.marks
        return data


class Teacher(Common):

    def __init__(self, first_name, last_name, department):
        super().__init__(first_name, last_name)
        self.department = department

    def profile_details(self):
        data = super().profile_details()
        data['department'] = self.department
        return data


"objects of Student class"
student_obj1 = Student("akshat", "shah", 98)
studnet_obj2 = Student("saiyam", "shah", 80)

print(student_obj1.profile_details())
print(studnet_obj2.profile_details())

"objects of Teacher class"
teacher_obj1 = Teacher("Diya", "patel", "maths")
teacher_obj2 = Teacher("Rakesh", "patel", "english")
teacher_obj3 = Teacher("jay", "patel", "computer")

print(teacher_obj1.profile_details())
print(teacher_obj2.profile_details())
print(teacher_obj3.profile_details())


print(f"Total Users {Common.count}")
