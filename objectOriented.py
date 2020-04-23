
# INIT METHOD Refrence geeksforgeeks.com

class students:
    def __init__(self, name, rollno, subject ,marks):
        self.name = name
        self.rollno = rollno
        self.subject = subject
        self.marks = marks

    def student_details(self):
        print('name of student :', self.name)
        print('Roll number is :', self.rollno)
        print('Subject is :', self.subject)
        print('Marks of student :', self.marks)

details = students('john', 420, 'Physics', 85)
details.student_details()