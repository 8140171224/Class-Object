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
