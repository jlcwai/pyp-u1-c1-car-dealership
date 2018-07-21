class Vehicle(object):
    def __init__(self, SALE_PRICE_MULTIPLIER, PURCHASE_PRICE_MULTIPLIER, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles


class Car(Vehicle):
    def __init__(self, SALE_PRICE_MULTIPLIER, PURCHASE_PRICE_MULTIPLIER, maker, model, year, base_price, miles):
      super(Car, self).__init__(SALE_PRICE_MULTIPLIER, PURCHASE_PRICE_MULTIPLIER, maker, model, year, base_price, miles)
      self.SALE_PRICE_MULTIPLIER = 1.2
      self.PURCHASE_PRICE_MULTIPLIER = 0.004


class Motorcycle(Vehicle):
    def __init__(self, SALE_PRICE_MULTIPLIER, PURCHASE_PRICE_MULTIPLIER, maker, model, year, base_price, miles):
      super(Motorcycle, self).__init__(SALE_PRICE_MULTIPLIER, PURCHASE_PRICE_MULTIPLIER, maker, model, year, base_price, miles)
      self.SALE_PRICE_MULTIPLIER = 1.1
      self.PURCHASE_PRICE_MULTIPLIER = 0.009


class Truck(Vehicle):
    def __init__(self, SALE_PRICE_MULTIPLIER, PURCHASE_PRICE_MULTIPLIER, maker, model, year, base_price, miles):
      super(Truck, self).__init__(SALE_PRICE_MULTIPLIER, PURCHASE_PRICE_MULTIPLIER, maker, model, year, base_price, miles)
      self.SALE_PRICE_MULTIPLIER = 1.6
      self.PURCHASE_PRICE_MULTIPLIER = 0.02
