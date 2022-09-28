#object orientated programming
#Object - a tangible thing, it can do stuff, can be described with attributes -- a NOUN

# #long way of doing it
cat1_data = {
    'color': 'black',
    'name': 'Midnight',
    'size': 'chonky'
}

cat2_data = {
    'color': 'orange',
    'name': 'Garfield',
    'size': 'lasagna'
}

cat3_data = {
    'color': 'green',
    'name': 'Lucky',
    'size': 'smol'
}

#attributes are data we hold in our class about a instance
#methods are things our objects can do
#make a class to concatinate class 'cat_data'

class Cat:
    # this constructor makes the object
    # def __init__(self,color,name,size):
    #     #create new attributes
    #     self.color = color
    #     self.name = name
    #     self.size = size

    all_cats = []
    cute = True
    def __init__(self, data, owner_name):
        self.color = data['color']
        self.name = data['name']
        self.size = data['size']
        self.cute = True
        self.owner = Human(owner_name)
        Cat.all_cats.append(self)

    # def __repr__(self):
    #     return (f"Hello my name is {self.name} I am a {self.color} {self.size} Cat, I live with {self.owner.name}")
        

    def print_info(self):
        print(f"Hello my name is {self.name} I am a {self.color} {self.size} Cat, I live with {self.owner.name}")
        return self

    def meow(self):
            print(f"{self.name} says meow")

    def bit_owner(self):
        print(f"{self.name} takes a bite out of {self.owner.name}")
        self.owner.yell()

    @classmethod #class methods have access to and can change attributes on the class level
    def print_all_cat_info(cls):
        for cat in cls.all_cats:
            cat.print_info()

    @classmethod
    def revolt(cls):
        for cat in cls.all_cats:
            cat.bit_owner()

    @staticmethod #cannot change anything (STATIC) hold some related functionality to the class
    def years_to_cat_years(years):
        return years * 7


class Human:
    def __init__(self, name):
        self.name = name

    def yell(self):
        print(f"{self.name} Yells out in pain")

human_1 = Human("jasmine")
human_2 = Human("Kevin")
human_3 = Human("Joe")

#cat1 is a data type of 'cat'
#These Lines create cat instances
cat1 = Cat(cat1_data, 'Jasmine')
cat2 = Cat(cat2_data, 'Kevin')
cat3 = Cat(cat3_data, 'Joe')

#These lines call the print info method for each cat instance
cat1.print_all_cat_info()
Cat.revolt()


