"""
This Module describes a class of Tank
"""


class Tank:
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'x' : 0, 'y': 0, 'z': 0}
        self._health = 100
        self.shoot = 20

    def accell(self, increase):
        self._speed += increase
        return None

    def decell(self, decrease):
        self._speed -= decrease
        return None

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def take_damage(self, amount):
        self._health -= amount
        return None

    # special methodes

    def get_health(self):
        return self._health

    # example fo set a method
    def set_health(self, new_health):
        self._health = new_health

    def __add__(self, other):
        return self._health + other._health

    #  special method for getting object information
    def __str__(self):
        return f"Health = {self._health}, Speed = {self._speed}"

    tank_health = property(get_health, set_health)

    # alternative way of
    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    # example fo set a method
    def tank_health(self, new_health):
        self._health = new_health
        return None


