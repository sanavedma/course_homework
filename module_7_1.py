class Product:
    def __init__(self, name, weight, category,  ):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add(self, *products):
        for product in products:
            string_product = (str(product))
            file = open(self.__file_name, 'r')
            file_reading = file.read()
            file.close()
            if string_product in file_reading:
                print(f'Продукт {string_product} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{string_product}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
