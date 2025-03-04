from new_student import Student

try:
    student = Student(name = "ouioui", surname = "LeTaxi")
    print(student.__repr__)
    student = Student(name = "Peter", surname = "agle", id = "toto")
    print(student)
except Exception as e:
    print(e)
# $> python tester.py
# Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
# ...
# TypeError: Student.__init__() got an unexpected keyword argument 'id