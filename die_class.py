from random import randint


class Die():

    def __init__(self,num):
        self.num_inside = num

    def roll(self):
        return randint(1, self.num_inside) # random function randint
