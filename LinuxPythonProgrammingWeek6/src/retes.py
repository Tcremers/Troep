'''
Created on Nov 2, 2016

@author: Tycho
'''
import re

def main():
    my_dict = {"name_1": 3, "name_2": 2, "name_3": 1}                  # simple dictionary
    my_dict_items = my_dict.items()                                     # .items() returns a list of (key, value) tuples from the dictionary
    print my_dict_items
    # produces output: [('name_2', 7), ('name_3', 5), ('name_1', 10)]
    
    # define a function that returns the part of each item we want to sort by
    def get_second(x):
        """returns the second item of x"""
        return x[1] 
    
    # pass the above function to the .sort() method with the keyword argument "key"
    # so that we sort the items by comparing the values at their second positions
    my_dict_items.sort(key=get_second)                                  # sort the list of tuples by what is contained in the second position of each tuple
    print my_dict_items                                                 # list is now sorted
    # produces output: [('name_3', 5), ('name_2', 7), ('name_1', 10)]
    
    # Everything in one line using sorted instead of sort
    print sorted(my_dict.items(), reverse = True, key=get_second) 
    # produces output: [('name_3', 5), ('name_2', 7), ('name_1', 10)]
    
    


if __name__ == '__main__':
    main()