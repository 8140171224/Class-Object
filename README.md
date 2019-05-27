# Class-Object
Python is an object oriented programming language. Unlike procedure oriented programming, where the main emphasis is on functions, object oriented programming stress on objects.  Object is simply a collection of data (variables) and methods (functions) that act on those data. And, class is a blueprint for the object.  We can think of class as a sketch (prototype) of a house. It contains all the details about the floors, doors, windows etc. Based on these descriptions we build the house. House is the object.  As, many houses can be made from a description, we can create many objects from a class. An object is also called an instance of a class and the process of creating this object is called instantiation

# class & object

# class computer

    class computer:

        #def function __init__
        def __init__(self,cpu,ram):
            self.cpu = cpu
            self.ram = ram
        # def function config
        def config(self):

            print('config is ;', self.cpu, self.ram)

    comp1 = computer('i5',8)
    comp2 = computer('r5',8)

    comp2.config()
    comp1.config()
##
##

# constructor
# self

        class computer:

             def __init__(self):
                self.name = 'aakash'
                self.age = 17
                 
             def update(self):

                self.age = 30

             def compare(self,other):

                 if self.age == other.age:
                     return True

                 else:
                     print('different')

                     return False

        c1 = computer()
        c1.age =50
        c2 = computer()


        if c1.compare(c2):
            print('same')

        print(c1.name)
        print(c2.name)

##
# inner class outer class
##


# outer class
        class student:

            def __init__(self,name,rollno):
                self.name = name
                self.rollno = rollno
                self.lap = self.Laptop()

            def show(self):

                print(self.name, self.rollno)
                self.lap.show()
# inner class
            class Laptop:

                def __init__(self):
                    self.brand = 'HP'
                    self.cpu = 'i5'
                    self.ram = 8

                def show(self):

                    print(self.brand, self.cpu, self.ram)


# con
        s1 = student('aakash',2)
        s2 = student('dhaval',1)

        print(s1.name, s1.rollno)

        s1.show()


# Information

## BY aakash padhiyar

## 8140171224
