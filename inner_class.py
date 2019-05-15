class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):

        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):

            print(self.brand, self.cpu, self.ram)


s1 = student('aakash',2)
s2 = student('dhaval',1)

print(s1.name, s1.rollno)

s1.show()


