class Bird:
    def intro(self):
        print("There are many types of birds")
    
    def fly(self):
        print("most of birds can fly but some cannot")
class Pigeon(Bird):
    def fly(self):
        print('Pigeons can fly')

class Penguin(Bird):
    def fly(self):
        print('Penguins cannot fly')



obj_bird=Bird()
obj_bird.intro()
obj_bird.fly()

obj_pign=Pigeon()
obj_pign.intro()
obj_pign.fly()

obj_peng=Penguin()
obj_peng.fly()

#numpy and pandas

