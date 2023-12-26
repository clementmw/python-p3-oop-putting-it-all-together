#!/usr/bin/env python3

class Shoe:
    def __init__ (self, brand, size):
        self.brand = brand

        if (type(size) in (int,float)):
            self.size = size
        else:
            print ("size must be an integer")

    def cobble(self):
        print ("says that the shoe has been repaired.")

    def test_cobble_makes_new(self):
        self.cobble()
        self.condition = "New"


Adidas = Shoe("Adidas", 9)

