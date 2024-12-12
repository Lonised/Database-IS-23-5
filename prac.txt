#Вариант 5

class Product:
    def __innit__(self, _name, _price, _quantity):
        self._name = _name
        self._price = _price
        self._quantity =_quantity

class Electronics(Product):
    def electro(self, apply_waranty):
        self.apply_waranty = apply_waranty
    return f("Электроника называется, " name = {_name}, "цена товара", price = {_price}, "качество товара", quantity = {_quantity}, "применение гарантий", apply_waranty = {apply_waranty})


class Clothing(Product):
    def cloth(self, fabric):
        self.fabric = fabric
    return f("Одежда называется, " name = {_name}, "цена товара", price = {_price}, "качество товара", quantity = {_quantity}, "ткань используемая для одежды", fabric = {fabric})


clas Grocery(Product):
    def groce(self, check_expiry_date):
        self.check_expiry_date = check_expiry_date
    return f("Продукт называется, " name = {_name}, "цена товара", price = {_price}, "качество товара", quantity = {_quantity}, "срок годности продукта", check_expiry_date = {check_expiry_date})



	

