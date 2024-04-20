"""cafeteria"""
RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }

class Track:
    """class track"""
    safety = True
    __beans = 5000
    __milk = 20000
    """class track"""
    MENU = {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    def __init__(self, date: str) -> None:
        """
        class object
        """
        self.date = date
        self.orders = []

    def place_order(self, order):
        """place an order"""
        if self.safety:
            if isinstance(order, Coffee) or isinstance(order, CustomCoffee):
                if order.name in self.MENU:
                    if order.milk > self.milk or order.espresso > self.beans*5:
                        return "Unfortunately, we don't have enough ingredients."
                    self.orders.append(order)
                    order.is_paid = True
                    order.price = self.MENU[order.name] * order.count
                    return 'Done!'
                return "Unfortunately, we don't have such kind of coffee in the menu."
            return "We can't create anything that is not a Coffee instance."
        return 'Unfortunately, now it is not safe to make coffee.'

    def milk_spoil(self, num: int):
        """spoil milk"""
        if num <= self.__milk:
            self.__milk -= num
        else:
            self.__milk = 0

    @classmethod
    def set_limit_milk(cls, num: int):
        """set milk limit"""
        cls.__milk = num

    @classmethod
    def change_air_state(cls):
        """air alarm"""
        if cls.safety is True:
            cls.safety = False
        else:
            cls.safety = True

    def total_revenue(self):
        """revenue"""
        return sum(obj.price for obj in self.orders)

    def total_milk(self):
        """milk"""
        return sum(obj.milk for obj in self.orders)

    def total_beans(self):
        """beans"""
        return sum(obj.espresso for obj in self.orders)/5

    @property
    def beans(self):
        """getter"""
        return int(self.__beans - self.total_beans())

    @property
    def milk(self):
        """getter"""
        if self.total_milk() < self.__milk:
            return int(self.__milk - self.total_milk())
        return 0

class Coffee:
    """class coffee"""
    __recipe = {}
    def __init__(self, name: str, count: int = 1) -> None:
        """class objects"""
        self.name = name
        self.count = count
        if len(Coffee.__recipe) != 0 and self.name in Coffee.__recipe:
            self.is_paid = False

    @property
    def espresso(self):
        """espresso"""
        return self.count * sum(value for key, value in Coffee.__recipe[self.name].items() \
if key == 'espresso')

    @property
    def milk(self):
        """milk"""
        return self.count * sum(value for key, value in Coffee.__recipe[self.name].items() \
if 'milk' in key)

    @classmethod
    def set_recipe(cls, recipe: dict)-> None:
        """sets coffee recipe"""
        cls.__recipe = recipe

    def __str__(self) -> str:
        """user message"""
        if len(self.__recipe) == 0:
            return 'Order cannot be created. Recipe has not been set.'
        if self.name not in self.__recipe:
            return "Order cannot be created. We don't have recipe for it."
        if not self.is_paid:
            return f'Order "{self.count} {self.name}" is created.'
        return f'Preparing {self.count} {self.name}...'

    def __repr__(self) -> str:
        """dev message"""
        return f'{self.count} {self.name}'

    def __eq__(self, cof: object) -> bool:
        """equvalence"""
        if isinstance(cof, CustomCoffee):
            return self.name == cof.name and self.count == cof.count and cof.flavor is False
        return self.name == cof.name and self.count == cof.count

class FlavorMixin:
    """class flavor mixing"""
    def add_flavor(self, sugar: int = 0, cinammon: bool = False, syrup: str = False):
        """adds flavor"""
        if self.is_paid:
            if self.count > 1:
                self.sugar = sugar * self.count
            else:
                self.sugar = sugar
            self.cinammon = cinammon
            self.syrup = syrup
            self.flavor = True
            return 'Done!'
        return 'Please, pay for it.'

class CustomCoffee(Coffee, FlavorMixin):
    """class custom coffee"""
    def __init__(self, name: str, count: int = 1) -> None:
        """objects"""
        Coffee.__init__(self, name, count)
        self.flavor = False

    def __str__(self) -> str:
        """user message"""
        if len(Coffee._Coffee__recipe) == 0:
            return 'Order cannot be created. Recipe has not been set.'
        if self.name not in Coffee._Coffee__recipe:
            return "Order cannot be created. We don't have recipe for it."
        if not self.is_paid:
            return f'Order "{self.count} custom {self.name}" is created.'
        if self.is_paid and self.flavor is False:
            return f'Preparing {self.count} {self.name}...'
        if self.is_paid and self.flavor is True:
            res = f'Your best {self.name} is ready! It has: '
            if self.sugar != 0:
                res += f'{self.sugar} stickers of sugar, '
            if self.cinammon is True:
                res += 'cinammon, '
            if self.syrup is not None:
                res += f'{self.syrup} syrup.'
            return res
        return ''

    def __repr__(self) -> str:
        """dev message"""
        return f'{self.count} custom {self.name}'

    def __eq__(self, cof: object) -> bool:
        """eq"""
        if isinstance(cof, Coffee):
            return self.name == cof.name and self.count == cof.count and self.flavor is False
        return self.name == cof.name and self.count == cof.count and self.sugar == cof.sugar and \
self.cinammon == cof.cinammon and self.syrup == cof.syrup
