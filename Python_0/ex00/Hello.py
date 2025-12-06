#!/usr/bin/env python3.10

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#first version

"""
ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "Luxembourg!")
ft_set = {"Hello", "Belval!"}
ft_dict = {"Hello" : "42Luxembourg!"}
"""

#second version
ft_list[1] = "World!"

#tuple immuable donc on doit le reassigner
ft_tuple = ("Hello", "Luxembourg!")

ft_dict["Hello"] = "42Luxembourg!"

ft_set.remove("tutu!")
ft_set.add("Belval!")

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)



