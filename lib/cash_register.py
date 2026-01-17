#!/usr/bin/env python3
import math


class CashRegister:
    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for item in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total -= math.floor(self.total * (self.discount/100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
