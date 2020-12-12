class Tree:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.age}, Height: {self.height}')

    def is_protected(self):
        if self.age >= 20 and self.height >= 20:
            print(f'Tree: {self.name} is protected')
            return

        print(f'Tree: {self.name} is not protected')

    def increase_age(self, value):
        self.age += value

tree_1 = Tree('Pine', 18, 32)
tree_2 = Tree('Birch', 48, 120)

tree_1.print_info()
tree_2.print_info()
tree_1.is_protected()
tree_2.is_protected()

tree_2.increase_age(1000)
tree_2.print_info()
