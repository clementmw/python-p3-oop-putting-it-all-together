#!/usr/bin/env python3
#has the title and page_count passed into __init__, and values can be set to new instance.

class Book:
    def __init__ (self,title,page_count):
        self.title = title
        if (type(page_count) in (int,float)):  # checks if page_count is an integer or float.   
            self.page_count = page_count
            print(self.title)
            print(self.page_count)
        else:
            print("page_count must be an integer")
   
men = Book("men", 23)       
    
        