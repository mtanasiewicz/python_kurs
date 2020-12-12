class Tree:
    name = 'Pine'
    age = 40
    height = 25

    def print_info(self):
        print(f'Nazwa: {self.name}, wiek: {self.age}, wysokość: {self.height}')

tree_1 = Tree()
info = tree_1.print_info()
info2 = Tree.print_info(tree_1)

print(info, info2)
