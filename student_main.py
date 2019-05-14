
class student:


    school = 'aakash'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):

        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def get_school(cls):
        return  cls.school

    def info():
        print("This is  student class.. in abc molude")


s1 = student(34,67,32)
s2 = student(89,45,12)

print(s1.avg())

print(student.get_school())
student.info()
