import random
class Card:
    def __init__(self,value,shape):
        self.value = value
        self.shape = shape

    cards = []

    def __str__(self):
        return f"{self.value} {self.shape}"