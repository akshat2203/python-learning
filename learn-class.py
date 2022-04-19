class Student:
    """
        Common base class for all Student
    """
    # todo: improve for Inheritance
    count = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.count += 1

    def student_count(self):
        print(f"Total student {Student.count}")

    def student_details(self):
        print(f"Name : {self.name} Marks: {self.marks}")


"objects of Student class"
student_obj = Student("Zara", 98)
studnet_obj2 = Student("Manni", 5000)

student_obj.student_count()
student_obj.student_details()
studnet_obj2.student_count()
studnet_obj2.student_details()

print(f"Total student {Student.count}")




