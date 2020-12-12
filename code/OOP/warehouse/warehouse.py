class Warehouse:

    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def print_available_products(self):
        for product in self.products:
            print(product)

    def add_product(self):
        product_name = input('Enter product name:')

        if product_name not in self.products:
            self.products.append(product_name)

    def remove_product(self):
        product_name = input('Enter product name:')

        if product_name in self.products:
            self.products.remove(product_name)
            print('Product removed')
        else:
            print('Product not found in warehouse')


warehouse = Warehouse(['Jabłko'])
warehouse.add_product()

warehouse.print_available_products()

warehouse.remove_product()
