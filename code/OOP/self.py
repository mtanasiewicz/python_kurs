class Tree:
    name = 'Pine'
    age = 40
    height = 25

    def print_info(self):
        print('Nazwa: {}, wiek: {}, wysokość: {}'.format(self.name, self.age, self.height))

tree_1 = Tree();
print(tree_1.print_info())