## Animal is-a object( yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

#Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        # class dog has-a name
        self.name = name
    # Cat is-a Animal
class Cat(Anima):
    def __init__(self, name)
    # cat has-a name
    self.name = name 

#Person is-a object
class Person(object):
    def __init__(self, name)
    # Person has-a name
    self.name = name 

    #Person has-a a pet of some kind
    self.pet = None

#Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
    # Employee has-a name, Be Manay employee nawy haya ka wary(inherits) grtwa la person we.
    super(Employee, self).__init__(name)
    # Employee has-a salary
    self.salary = salary

# class fish is-a object
class fish(object):
    pass

# class salamon is-a fish
class salamon(fish):
    pass

#class halibut is-a fish
class halibut(fish):
    pass

#Rover is-a dog
rover = Cat("Rover")

#satan is-a Cat
satan = Cat("Satan")

# Mary is-a Person
mary = Person("Mary")

# marry has-a pet cat named is-a satan
mary.pet = satan

#Frank is-a employee has-a salary 120000
frank = Employee("Frank", 120000)

#flipper is-a instance of fish()
flipper = fish()