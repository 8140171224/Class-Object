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



