class Warehouse:

    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def print_available_products(self):
        for product in self.products:
            print(product)

        print('\n')

    def add_product(self):
        product_name = input('Enter product name:')

        if product_name not in self.products:
            self.products.append(product_name)
            print(f'Dodano produkt {product_name}\n')
        else:
            print('Produkt już istnieje\n')

    def remove_product(self):
        product_name = input('Enter product name:')

        if product_name in self.products:
            self.products.remove(product_name)
            print('Product removed')
        else:
            print('Product not found in warehouse')


warehouse = Warehouse()

while True:
    print('Aby dodać produkt do magazyzynu, wciśnij 1\n'
          'Aby usunąć produkt z magazynu wciśnij 2 \n'
          'Aby wyświetlić wszystkie produkty wciśnij 3\n'
          'Aby wyjść wciśnij Q \n\n')

    choice = input()
    if choice.lower() == 'q':
        exit('koniec')
    elif choice == '1':
        warehouse.add_product()
        continue
    elif choice == '2':
        warehouse.remove_product()
    elif choice == '3':
        warehouse.print_available_products()