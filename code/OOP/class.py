class Tree:
    name = 'Pine'
    age = 40
    height = 25

tree_1 = Tree()
tree_2 = Tree()
print(tree_1, tree_2)
print(id(tree_1), id(tree_2))
print(dir(tree_1))
print(tree_1.height)

tree_1.condition = 'Good'
print(dir(tree_1))